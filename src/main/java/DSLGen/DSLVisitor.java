package DSLGen;

import GeneratedQEGrammar.QEDocParser;
import GeneratedQEGrammar.QEDocParserBaseVisitor;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;
import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DSLVisitor extends QEDocParserBaseVisitor<StringBuilder> {
    public final HashMap<String, ClassInternal> pythonClasses;
    // Because ANTLR4 set the method arguments to be only the context, to pass other arguments,
    // I have to manually set up a call stack.
    private final Stack<ClassInternal> classStack;
    private final Stack<MemberInternal> memberStack;
    private int choiceCounter = 0;
    private int groupCounter = 0;
    private int undocumentedCounter = 0;
    public ClassInternal topLevelClass;
    private final ClassInternal nameListClass = new ClassInternal("NameList");
    private final ClassInternal cardClass = new ClassInternal("Card");
    private final ClassInternal optionsClass = new ClassInternal("Options");
    private final ClassInternal chooseClass = new ClassInternal("Choose");
    private final ClassInternal groupClass = new ClassInternal("Group");
    private final ClassInternal rowClass = new ClassInternal("Row");
    private final ClassInternal choiceClass = new ClassInternal("Choice");

    public DSLVisitor() {
        pythonClasses = new HashMap<>();
        classStack = new Stack<>();
        memberStack = new Stack<>();
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (Map.Entry<String, ClassInternal> entry : pythonClasses.entrySet()) {
            builder.append(entry.getValue().toString()).append("\n");
        }
        return builder.toString();
    }

    private StringBuilder withClass(Function<ClassInternal, StringBuilder> f) {
        ClassInternal pc = classStack.pop();
        StringBuilder builder = f.apply(pc);
        classStack.push(pc);
        return builder;
    }

    private StringBuilder withMember(Function<MemberInternal, StringBuilder> f) {
        MemberInternal pm = memberStack.pop();
        StringBuilder builder = f.apply(pm);
        memberStack.push(pm);
        return builder;
    }

    private ClassInternal newClass(ClassInternal newPc, ClassInternal pc, ClassType type) {
        pc.imports.add(newPc);
        switch (type) {
            case NAMELIST: newPc.addInherit(nameListClass);
            case CARD: newPc.addInherit(cardClass);
            case OPTIONS: newPc.addInherit(optionsClass);
            case CHOOSE: newPc.addInherit(chooseClass);
            case GROUP: newPc.addInherit(groupClass);
            case ROW: newPc.addInherit(rowClass);
            case CHOICE: newPc.addInherit(choiceClass);
            default:
        }
        classStack.push(newPc);
        return newPc;
    }

    private MemberInternal newMember(MemberInternal newPm, ClassInternal pc) {
        pc.members.add(newPm);
        memberStack.push(newPm);
        return newPm;
    }

    private void completeClass() {
        ClassInternal complete = classStack.pop();
        pythonClasses.put(complete.name.toString(), complete);
    }

    private void completeMember() {
        memberStack.pop();
    }

    @Override
    protected StringBuilder aggregateResult(StringBuilder aggregate, StringBuilder nextResult) {
        if (aggregate == null) return nextResult;
        else if (nextResult == null) return aggregate;
        else return aggregate.append(" ").append(nextResult);
    }

    @Override
    public StringBuilder visitDef(QEDocParser.DefContext ctx) {
        return super.visitDef(ctx);
    }

    @Override
    public StringBuilder visitBlock(QEDocParser.BlockContext ctx) {
        return super.visitBlock(ctx);
    }

    @Override
    public StringBuilder visitIntroBlock(QEDocParser.IntroBlockContext ctx) {
        return withClass(pc -> pc.intro.append(super.visitIntroBlock(ctx)));
    }

    @Override
    public StringBuilder visitDefaultBlock(QEDocParser.DefaultBlockContext ctx) {
        return withMember(pm -> pm.defaultString.append(super.visitDefaultBlock(ctx)));
    }

    @Override
    public StringBuilder visitInfoBlock(QEDocParser.InfoBlockContext ctx) {
        return withMember(pm -> pm.info.append(super.visitInfoBlock(ctx)));
    }

    @Override
    public StringBuilder visitOptBlock(QEDocParser.OptBlockContext ctx) {
        return withClass(pec -> {
            String enumName = getSwitch(ctx.OptBegin(), "val");
            assert enumName != null;
            StringBuilder enumText = visit(ctx.textBlockBody());
            pec.enums.put(enumName.replace("{", "").trim(),
                    enumText != null? enumText: new StringBuilder("Undocumented ").append(undocumentedCounter++));
            return null;
        });
    }

    @Override
    public StringBuilder visitStatusBlock(QEDocParser.StatusBlockContext ctx) {
        return super.visitStatusBlock(ctx);
    }

    @Override
    public StringBuilder visitTextBlock(QEDocParser.TextBlockContext ctx) {
        return super.visitTextBlock(ctx);
    }

    @Override
    public StringBuilder visitLabelBlock(QEDocParser.LabelBlockContext ctx) {
        return withClass(pc -> pc.label.append(super.visitLabelBlock(ctx)));
    }

    @Override
    public StringBuilder visitMessageBlock(QEDocParser.MessageBlockContext ctx) {
        return withClass(pc -> pc.message.append(super.visitMessageBlock(ctx)));
    }

    @Override
    public StringBuilder visitTocBlock(QEDocParser.TocBlockContext ctx) {
        return withClass(pc -> {
            pc.toc = true;
            return null;
        });
    }

    @Override
    public StringBuilder visitSeeBlock(QEDocParser.SeeBlockContext ctx) {
        return super.visitSeeBlock(ctx);
    }

    @Override
    public StringBuilder visitEnumBlock(QEDocParser.EnumBlockContext ctx) {
        return withClass(pc -> withMember(pm -> {
                    if (pythonClasses.get(String.format("%s_options", pm.name)) != null) return null;
                    ClassInternal enumClass = newClass(new ClassInternal(String.format("%s_options", pm.name)), pc, ClassType.OPTIONS);
                    pm.type = enumClass.name;
                    String enumText = ctx.textBlockBody().getText()
                            .replace("{", "").replace("}", "");
                    for (String opt : enumText.split("\\|"))
                        enumClass.enums.put(opt.trim(), new StringBuilder(opt.trim()));
                    completeClass();
                    return null;
                })
        );
    }

    @Override
    public StringBuilder visitTextBlockBody(QEDocParser.TextBlockBodyContext ctx) {
        return super.visitTextBlockBody(ctx);
    }

    @Override
    public StringBuilder visitRef(QEDocParser.RefContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitBoldText(QEDocParser.BoldTextContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitIText(QEDocParser.ITextContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitTTText(QEDocParser.TTTextContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitStringText(QEDocParser.StringTextContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitLogicalText(QEDocParser.LogicalTextContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitScopedText(QEDocParser.ScopedTextContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitWordText(QEDocParser.WordTextContext ctx) {
        return new StringBuilder(ctx.getText());
    }

    @Override
    public StringBuilder visitCardBlock(QEDocParser.CardBlockContext ctx) {
        return withClass(pc -> {
            ClassInternal cardClass = newClass(new ClassInternal(ctx.structureBlockBody().ID().getText()), pc, ClassType.CARD);

            super.visitCardBlock(ctx);
            newMember(new MemberInternal(String.format("card_%s", cardClass.name), cardClass.name.toString()), pc);
            completeMember();
            completeClass();
            return null;
        });
    }

    @Override
    public StringBuilder visitCardFlagBlock(QEDocParser.CardFlagBlockContext ctx) {
        withClass(pc -> {
            String enumName = ctx.structureBlockBody().ID().toString();
            newMember(new MemberInternal(String.format("flag_%s", enumName), ""), pc);
            return null;
        });
        super.visitCardFlagBlock(ctx);
        completeMember();
        return null;
    }

    @Override
    public StringBuilder visitChooseBlock(QEDocParser.ChooseBlockContext ctx) {
        return withClass(pc -> {
            ClassInternal choiceClass = newClass(new ClassInternal(String.format("Choice%d", choiceCounter++)), pc, ClassType.CHOOSE);
            super.visitChooseBlock(ctx);
            newMember(new MemberInternal(choiceClass.name.toString().toLowerCase(), choiceClass.name.toString()), pc);
            completeClass();
            return null;
        });
    }

    @Override
    public StringBuilder visitColBlock(QEDocParser.ColBlockContext ctx) {
        withClass(pc -> {
            String typeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
            newMember(new MemberInternal(ctx.structureBlockBody().ID().toString(), typeName), pc);
            return null;
        });
        super.visitColBlock(ctx);
        completeMember();
        return null;
    }

    @Override
    public StringBuilder visitColGroupBlock(QEDocParser.ColGroupBlockContext ctx) {
        return withClass(pc -> {
            String typeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
            MemberInternal template = newMember(new MemberInternal("",
                    typeName != null ? typeName : "STRING"), new ClassInternal(""));

            for (QEDocParser.BlockContext c : ctx.structureBlockBody().block()) {
                if (c.plainTextBlock() != null) visit(c);
            }
            completeMember();

            for (QEDocParser.BlockContext c : ctx.structureBlockBody().block()) {
                if (c.smartAssBlock() != null) {
                    newMember(new MemberInternal(template), pc);
                    visit(c);
                    completeMember();
                }
            }
            return null;
        });
    }

    @Override
    public StringBuilder visitColsBlock(QEDocParser.ColsBlockContext ctx) {
        withClass(pc -> {
            pc.name.append("_").append("col");
            for (TerminalNode t : ctx.structureBlockBody().SwitchText()) {
                pc.others.append(t.getText());
            }
            return null;
        });
        super.visitColsBlock(ctx);
        return null;
    }

    @Override
    public StringBuilder visitConditionalBlock(QEDocParser.ConditionalBlockContext ctx) {
        return super.visitConditionalBlock(ctx);
    }

    @Override
    public StringBuilder visitDimBlock(QEDocParser.DimBlockContext ctx) {
        return withClass(pc -> {
            MemberInternal pm = newMember(new MemberInternal(ctx.structureBlockBody().ID().toString(), ""), pc);
            String startIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "start");
            String endIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "end");
            pm.others.append(String.format("Start - %s; ", startIndex))
                    .append(String.format("End - %s\n", endIndex));
            String baseTypeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
            pm.type.append(String.format("List %s", baseTypeName));
            super.visitDimBlock(ctx);
            completeMember();
            return null;
        });
    }

    @Override
    public StringBuilder visitDimensionGroupBlock(QEDocParser.DimensionGroupBlockContext ctx) {
        return withClass(pc -> {
            String startIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "start");
            String endIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "end");
            String baseTypeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");

            MemberInternal template = newMember(new MemberInternal(
                    "", String.format("List %s", baseTypeName)), new ClassInternal(""));
            template.others.append(String.format("Start - %s; ", startIndex))
                    .append(String.format("End - %s", endIndex));

            return visitGroup(pc, template, ctx.structureBlockBody());
        });
    }

    private StringBuilder visitGroup(ClassInternal pc, MemberInternal template, QEDocParser.StructureBlockBodyContext structureBlockBodyContext) {
        for (QEDocParser.BlockContext c : structureBlockBodyContext.block())
            if (c.plainTextBlock() != null) visit(c);


        for (QEDocParser.BlockContext c : structureBlockBodyContext.block()) {
            if (c.smartAssBlock() != null) {
                newMember(new MemberInternal(template), pc);
                visit(c);
                completeMember();
            }
        }

        completeMember();
        return null;
    }

    @Override
    public StringBuilder visitElseWhenBlock(QEDocParser.ElseWhenBlockContext ctx) {
        return visitConditional(ctx, ctx.structureBlockBody(),
                c -> super.visitElseWhenBlock((QEDocParser.ElseWhenBlockContext) c));
    }

    @Override
    public StringBuilder visitGroupBlock(QEDocParser.GroupBlockContext ctx) {
        return withClass(pc -> {
            newClass(new ClassInternal(String.format("Group%d", groupCounter++)), pc, ClassType.GROUP);

            for (QEDocParser.BlockContext c : ctx.structureBlockBody().block())
                if (c.plainTextBlock() != null) visit(c);

            for (QEDocParser.BlockContext c : ctx.structureBlockBody().block())
                if (c.structureBlock() != null) visit(c);

            completeClass();
            return null;
        });
    }

    @Override
    public StringBuilder visitInputDescriptionBlock(QEDocParser.InputDescriptionBlockContext ctx) {
        // Top level
        StringBuilder className = new StringBuilder();
        String programName = getSwitch(ctx.structureBlockBody().SwitchText(), "program");
        assert programName != null;
        className.append(programName);
        ClassInternal pc = new ClassInternal(className.toString());
        topLevelClass = pc;
        pythonClasses.put(pc.name.toString(), pc);
        classStack.push(pc);

        super.visitInputDescriptionBlock(ctx);

        classStack.pop();
        return null;
    }

    @Override
    public StringBuilder visitLineBlock(QEDocParser.LineBlockContext ctx) {
        return super.visitLineBlock(ctx);
    }

    @Override
    public StringBuilder visitNameListBlock(QEDocParser.NameListBlockContext ctx) {
        return withClass(pc -> {
            String className = ctx.structureBlockBody().ID().toString();

            newClass(new ClassInternal(className), pc, ClassType.NAMELIST);
            super.visitNameListBlock(ctx);
            completeClass();

            newMember(new MemberInternal(String.format("namelist_%s", className), className), pc);
            completeMember();

            return null;
        });
    }

    @Override
    public StringBuilder visitOptionalBlock(QEDocParser.OptionalBlockContext ctx) {
        return super.visitOptionalBlock(ctx);
    }

    @Override
    public StringBuilder visitOptionsBlock(QEDocParser.OptionsBlockContext ctx) {
        return withClass(pc -> withMember(pm -> {
            String name = String.format("%s_options", pm.name);
            if (pythonClasses.get(name) != null) pythonClasses.remove(name);
            ClassInternal optionClass = newClass(new ClassInternal(name), pc, ClassType.OPTIONS);
            pm.type = optionClass.name;

            for (QEDocParser.BlockContext c : ctx.structureBlockBody().block()) {
                if (c.plainTextBlock() == null) continue;
                MemberInternal npm = newMember(new MemberInternal("", ""), new ClassInternal(""));
                visit(c);
                completeMember();
                optionClass.others.append(npm.info);
            }
            completeClass();
            return null;
        }));

    }

    @Override
    public StringBuilder visitOtherwiseBlock(QEDocParser.OtherwiseBlockContext ctx) {
        return visitConditional(ctx, ctx.structureBlockBody(),
                c -> super.visitOtherwiseBlock((QEDocParser.OtherwiseBlockContext) c));
    }

    @Override
    public StringBuilder visitRowBlock(QEDocParser.RowBlockContext ctx) {
        return withClass(pc -> {
            String typeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
            newMember(new MemberInternal(
                    ctx.structureBlockBody().ID().toString(), typeName), pc);
            completeMember();

            return super.visitRowBlock(ctx);
        });
    }

    @Override
    public StringBuilder visitRowGroupBlock(QEDocParser.RowGroupBlockContext ctx) {
        return visitRowOrColGroupBlock(ctx.structureBlockBody());

    }

    private StringBuilder visitRowOrColGroupBlock(QEDocParser.StructureBlockBodyContext ctx) {
        return withClass(pc -> {
            String typeName = getSwitch(ctx.SwitchText(), "type");
            MemberInternal template = newMember(new MemberInternal("",
                            typeName != null ? typeName : "STRING"),
                    new ClassInternal(""));

            return visitGroup(pc, template, ctx);
        });
    }

    @Override
    public StringBuilder visitRowsBlock(QEDocParser.RowsBlockContext ctx) {
        withClass(pc -> {
            pc.name.append("_").append("row");
            for (TerminalNode t : ctx.structureBlockBody().SwitchText())
                pc.others.append(t.getText());
            return null;
        });
        return super.visitRowsBlock(ctx);
    }

    @Override
    public StringBuilder visitSectionBlock(QEDocParser.SectionBlockContext ctx) {
        System.err.printf("Section is not implemented: %s.%n",
                ctx.structureBlockBody().SwitchText(0).getText());
        return null;
    }

    @Override
    public StringBuilder visitSubsectionBlock(QEDocParser.SubsectionBlockContext ctx) {
        System.err.printf("Section is not implemented: %s.%n",
                ctx.structureBlockBody().SwitchText(0).getText());
        return null;
    }

    @Override
    public StringBuilder visitSyntaxBlock(QEDocParser.SyntaxBlockContext ctx) {
        return super.visitSyntaxBlock(ctx);
    }

    @Override
    public StringBuilder visitTableBlock(QEDocParser.TableBlockContext ctx) {
        return withClass(pc -> {
            ClassInternal tableClass = newClass(new ClassInternal(ctx.structureBlockBody().ID().toString()),
                    pc, ClassType.ROW);
            super.visitTableBlock(ctx);
            completeClass();
            newMember(new MemberInternal(ctx.Table().getText(),
                    String.format("List %s", tableClass.name.toString())), pc);
            completeMember();
            return null;
        });
    }

    private String getSwitch(TerminalNode text, String switchName) {
        Pattern varTypeBuilderSwitchRegex = Pattern.compile(
                String.format("-%s\\s+(.+)", switchName), Pattern.CASE_INSENSITIVE);
        Matcher m = varTypeBuilderSwitchRegex.matcher(text.toString());
        if (m.find()) {
            return m.group(1).trim();
        } else {
            return null;
        }
    }

    private String getSwitch(List<TerminalNode> switches, String switchName) {
        for (TerminalNode text : switches) {
            String result = getSwitch(text, switchName);
            if (result != null) return result;
        }
        return null;
    }

    @Override
    public StringBuilder visitVarBlock(QEDocParser.VarBlockContext ctx) {
        withClass(pc -> {
            String typeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
            newMember(new MemberInternal(ctx.structureBlockBody().ID().toString(), typeName), pc);
            return null;
        });
        super.visitVarBlock(ctx);
        return null;
    }

    @Override
    public StringBuilder visitVarGroupBlock(QEDocParser.VarGroupBlockContext ctx) {
        return visitRowOrColGroupBlock(ctx.structureBlockBody());
    }

    private StringBuilder visitConditional(QEDocParser.StructureBlockContext ctx,
                                           QEDocParser.StructureBlockBodyContext ctxBody,
                                           Function<QEDocParser.StructureBlockContext, StringBuilder> visit) {
        return withClass(pc -> {
            String predicate = getSwitch(ctxBody.SwitchText(), "test");
            ClassInternal predicateClass = newClass(new ClassInternal(String.format("%s %s",
                    predicate != null ? predicate : "Otherwise", pc.name)), pc, ClassType.CHOICE);
            predicateClass.addInherit(pc);
            visit.apply(ctx);
            completeClass();
            return null;
        });

    }

    @Override
    public StringBuilder visitWhenBlock(QEDocParser.WhenBlockContext ctx) {
        return visitConditional(ctx, ctx.structureBlockBody(),
                c -> super.visitWhenBlock((QEDocParser.WhenBlockContext) c));

    }

    @Override
    public StringBuilder visitStructureBlockBody(QEDocParser.StructureBlockBodyContext ctx) {
        return super.visitStructureBlockBody(ctx);
    }

    @Override
    public StringBuilder visitSmartIntroBlock(QEDocParser.SmartIntroBlockContext ctx) {
        return super.visitSmartIntroBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartOptBlock(QEDocParser.SmartOptBlockContext ctx) {
        return super.visitSmartOptBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartDefaultBlock(QEDocParser.SmartDefaultBlockContext ctx) {
        return super.visitSmartDefaultBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartInfoBlock(QEDocParser.SmartInfoBlockContext ctx) {
        return super.visitSmartInfoBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartStatusBlock(QEDocParser.SmartStatusBlockContext ctx) {
        return super.visitSmartStatusBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartTextBlock(QEDocParser.SmartTextBlockContext ctx) {
        return super.visitSmartTextBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartLabelBlock(QEDocParser.SmartLabelBlockContext ctx) {
        return super.visitSmartLabelBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartMessageBlock(QEDocParser.SmartMessageBlockContext ctx) {
        return super.visitSmartMessageBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartEnumBlock(QEDocParser.SmartEnumBlockContext ctx) {
        return super.visitSmartEnumBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartTocBlock(QEDocParser.SmartTocBlockContext ctx) {
        return super.visitSmartTocBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartSeeBlock(QEDocParser.SmartSeeBlockContext ctx) {
        return super.visitSmartSeeBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartCardBlock(QEDocParser.SmartCardBlockContext ctx) {
        return super.visitSmartCardBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartCardFlagBlock(QEDocParser.SmartCardFlagBlockContext ctx) {
        return super.visitSmartCardFlagBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartChooseBlock(QEDocParser.SmartChooseBlockContext ctx) {
        return super.visitSmartChooseBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartColBlock(QEDocParser.SmartColBlockContext ctx) {
        return withMember(pm -> {
            pm.name = new StringBuilder(ctx.ID().getText());
            return null;
        });
    }

    @Override
    public StringBuilder visitSmartColGroupBlock(QEDocParser.SmartColGroupBlockContext ctx) {
        return super.visitSmartColGroupBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartColsBlock(QEDocParser.SmartColsBlockContext ctx) {
        return super.visitSmartColsBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartConditionalBlock(QEDocParser.SmartConditionalBlockContext ctx) {
        return super.visitSmartConditionalBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartDimBlock(QEDocParser.SmartDimBlockContext ctx) {
        return withMember(pm -> {
            pm.name = new StringBuilder(ctx.ID().getText());
            super.visitSmartDimBlock(ctx);
            return null;
        });
    }

    @Override
    public StringBuilder visitSmartDimensionGroupBlock(QEDocParser.SmartDimensionGroupBlockContext ctx) {
        return super.visitSmartDimensionGroupBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartElseWhenBlock(QEDocParser.SmartElseWhenBlockContext ctx) {
        return super.visitSmartElseWhenBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartGroupBlock(QEDocParser.SmartGroupBlockContext ctx) {
        return super.visitSmartGroupBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartLineBlock(QEDocParser.SmartLineBlockContext ctx) {
        return super.visitSmartLineBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartNameListBlock(QEDocParser.SmartNameListBlockContext ctx) {
        return super.visitSmartNameListBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartOptionalBlock(QEDocParser.SmartOptionalBlockContext ctx) {
        return super.visitSmartOptionalBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartOptionsBlock(QEDocParser.SmartOptionsBlockContext ctx) {
        return super.visitSmartOptionsBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartOtherwiseBlock(QEDocParser.SmartOtherwiseBlockContext ctx) {
        return super.visitSmartOtherwiseBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartRowGroupBlock(QEDocParser.SmartRowGroupBlockContext ctx) {
        return super.visitSmartRowGroupBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartRowBlock(QEDocParser.SmartRowBlockContext ctx) {
        return withMember(pm -> {
            pm.name = new StringBuilder(ctx.ID().getText());
            return null;
        });
    }

    @Override
    public StringBuilder visitSmartRowsBlock(QEDocParser.SmartRowsBlockContext ctx) {
        return super.visitSmartRowsBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartSectionBlock(QEDocParser.SmartSectionBlockContext ctx) {
        return super.visitSmartSectionBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartSubsectionBlock(QEDocParser.SmartSubsectionBlockContext ctx) {
        return super.visitSmartSubsectionBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartSyntaxBlock(QEDocParser.SmartSyntaxBlockContext ctx) {
        return super.visitSmartSyntaxBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartTableBlock(QEDocParser.SmartTableBlockContext ctx) {
        return super.visitSmartTableBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartVarGroupBlock(QEDocParser.SmartVarGroupBlockContext ctx) {
        return super.visitSmartVarGroupBlock(ctx);
    }

    @Override
    public StringBuilder visitSmartVarBlock(QEDocParser.SmartVarBlockContext ctx) {
        return withMember(pm -> {
            pm.name = new StringBuilder(ctx.ID().getText());
            return null;
        });
    }

    @Override
    public StringBuilder visitSmartWhenBlock(QEDocParser.SmartWhenBlockContext ctx) {
        return super.visitSmartWhenBlock(ctx);
    }
}
