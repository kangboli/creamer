package DSLGen;

import GeneratedQEGrammar.QEDocParser;
import GeneratedQEGrammar.QEDocParserBaseVisitor;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.util.*;
import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DSLVisitor extends QEDocParserBaseVisitor<StringBuilder> {
    private final String outputDir;
    private final HashMap<String, PythonClass> pythonClasses;
    // Because ANTLR4 set the method arguments to be only the context, to pass other arguments,
    // I have to manually set up a call stack.
    private final Stack<PythonClass> classStack;
    private final Stack<PythonMember> memberStack;
    private int choiceCounter = 0;
    private int groupCounter = 0;

    public DSLVisitor(String outputDir) {
        this.outputDir = outputDir;
        pythonClasses = new HashMap<>();
        classStack = new Stack<>();
        memberStack = new Stack<>();
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (Map.Entry<String, PythonClass> entry: pythonClasses.entrySet()) {
            builder.append(entry.getValue().toString()).append("\n");
        }
        return builder.toString();
    }

    private StringBuilder withClass(Function<PythonClass, StringBuilder> f) {
        PythonClass pc = classStack.pop();
        StringBuilder builder = f.apply(pc);
        classStack.push(pc);
        return builder;
    }
    private PythonMember newMember(PythonMember newPc, PythonClass pc) {
        pc.members.add(newPc);
        memberStack.push(newPc);
        return newPc;
    }

    private void completeMember() {
        memberStack.pop();
    }

    private PythonClass newClass(PythonClass newPc, PythonClass pc) {
        pc.imports.add(newPc);
        classStack.push(newPc);
        return newPc;
    }

    private void completeClass() {
        PythonClass complete = classStack.pop();
        pythonClasses.put(complete.name.toString(), complete);
    }

    private StringBuilder withMember(Function<PythonMember, StringBuilder> f) {
        PythonMember pm = memberStack.pop();
        StringBuilder builder = f.apply(pm);
        memberStack.push(pm);
        return builder;
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
    public StringBuilder visitIntroBlock(QEDocParser.IntroBlockContext ctx) { return withClass(pc ->
            pc.intro.append("Intro:\n").append(super.visitIntroBlock(ctx)).append("\n")
    );}

    @Override
    public StringBuilder visitDefaultBlock(QEDocParser.DefaultBlockContext ctx) { return withMember(pm ->
            pm.defaultString.append("Default: ").append(super.visitDefaultBlock(ctx)).append("\n")
    );}

    @Override
    public StringBuilder visitInfoBlock(QEDocParser.InfoBlockContext ctx) { return withMember(pm ->
            pm.info.append("Info:\n").append(super.visitInfoBlock(ctx)).append("\n")
    );}

    @Override
    public StringBuilder visitOptBlock(QEDocParser.OptBlockContext ctx) { return withClass(pec -> {
        String enumName = getSwitch(ctx.OptBegin(), "val");
        assert enumName != null;
        ((PythonEnumClass) pec).enums.put(escape(enumName.replace("{", "").trim()),
                visit(ctx.textBlockBody()));
        return null;
    });}

    @Override
    public StringBuilder visitStatusBlock(QEDocParser.StatusBlockContext ctx) {
        return super.visitStatusBlock(ctx);
    }

    @Override
    public StringBuilder visitTextBlock(QEDocParser.TextBlockContext ctx) {
        return super.visitTextBlock(ctx);
    }

    @Override
    public StringBuilder visitLabelBlock(QEDocParser.LabelBlockContext ctx) { return withClass(pc -> {
        pc.label.append(super.visitLabelBlock(ctx));
        return null;
    });}

    @Override
    public StringBuilder visitMessageBlock(QEDocParser.MessageBlockContext ctx) { return withClass(pc -> {
        pc.message.append(super.visitMessageBlock(ctx));
        return null;
    });}

    @Override
    public StringBuilder visitTocBlock(QEDocParser.TocBlockContext ctx) { return withClass(pc -> {
        pc.toc = true;
        return null;
    });}

    @Override
    public StringBuilder visitSeeBlock(QEDocParser.SeeBlockContext ctx) {
        return super.visitSeeBlock(ctx);
    }

    @Override
    public StringBuilder visitEnumBlock(QEDocParser.EnumBlockContext ctx) { return withClass(pc -> withMember(pm -> {
                if (pythonClasses.get(String.format("%s_options", pm.name)) != null) return null;
                PythonClass enumClass = newClass(new PythonEnumClass(String.format("%s_options", pm.name)), pc);
                pm.type = enumClass.name;
                String enumText = ctx.textBlockBody().getText()
                        .replace("{", "").replace("}", "");
                for (String opt : enumText.split("\\|"))
                    ((PythonEnumClass) enumClass).enums.put(opt.trim(), new StringBuilder(opt.trim()));
                completeClass();
                return  null;
            })
    );}

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
    public StringBuilder visitCardBlock(QEDocParser.CardBlockContext ctx) { return withClass(pc -> {
            PythonClass cardClass = newClass(new PythonClass(ctx.structureBlockBody().ID().getText()), pc);

            super.visitCardBlock(ctx);
            newMember(new PythonMember(String.format("card_%s", cardClass.name), cardClass.name.toString()), pc);
            completeMember();
            completeClass();
            return null;
        });
    }

    @Override
    public StringBuilder visitCardFlagBlock(QEDocParser.CardFlagBlockContext ctx) {
        withClass(pc -> {
            String enumName = ctx.structureBlockBody().ID().toString();
            newMember(new PythonMember(String.format("flag_%s", enumName), ""), pc);
            return null;
        });
        super.visitCardFlagBlock(ctx);
        completeMember();
        return null;
    }

    @Override
    public StringBuilder visitChooseBlock(QEDocParser.ChooseBlockContext ctx) {
        return withClass(pc -> {
            choiceCounter++;
            PythonClass choiceClass = newClass(new PythonClass(String.format("Choice%d", choiceCounter)), pc);
            super.visitChooseBlock(ctx);
            newMember(new PythonMember(choiceClass.name.toString().toLowerCase(), choiceClass.name.toString()), pc);
            completeClass();
            return null;
        });
    }

    @Override
    public StringBuilder visitColBlock(QEDocParser.ColBlockContext ctx) {
        withClass(pc -> {
            String typeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
            newMember(new PythonMember(ctx.structureBlockBody().ID().toString(), translateType(typeName)), pc);
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
            PythonMember template  = newMember(new PythonMember("",
                    translateType(escape(typeName != null ? typeName : "STRING"))), new PythonClass(""));

            for (QEDocParser.BlockContext c: ctx.structureBlockBody().block()) {
                if (c.plainTextBlock() != null)  visit(c);
            }
            completeMember();

            for (QEDocParser.BlockContext c: ctx.structureBlockBody().block()) {
                if (c.smartAssBlock() != null) {
                    newMember(new PythonMember(template), pc);
                    visit(c);
                    completeMember();
                }
            }
            return null;
        });
    }

    @Override
    public StringBuilder visitColsBlock(QEDocParser.ColsBlockContext ctx) {
        withClass(pc->{
            pc.name.append("_").append("col");
            for (TerminalNode t: ctx.structureBlockBody().SwitchText()) {
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

    private static String translateType(String type) {
        return switch (type) {
            case "REAL" -> "float";
            case "INTEGER" -> "int";
            case "LOGICAL" -> "bool";
            default -> "string";
        };
    }
    @Override
    public StringBuilder visitDimBlock(QEDocParser.DimBlockContext ctx) { return withClass(pc -> {
        PythonMember pm = newMember(new PythonMember(ctx.structureBlockBody().ID().toString(), ""), pc);
        String startIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "start");
        String endIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "end");
        pm.others.append(String.format("Start: %s\n", startIndex))
                .append(String.format("End: %s\n", endIndex));
        String baseTypeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
        pm.type.append(String.format("List[%s]", translateType(baseTypeName)));
        super.visitDimBlock(ctx);
        completeMember();
        return null;
    });}

    @Override
    public StringBuilder visitDimensionGroupBlock(QEDocParser.DimensionGroupBlockContext ctx) { return withClass(pc -> {
        String startIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "start");
        String endIndex = getSwitch(ctx.structureBlockBody().SwitchText(), "end");
        String baseTypeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");

        PythonMember template = newMember(new PythonMember(
                "", String.format("List[%s]", translateType(baseTypeName))), new PythonClass(""));
        template.others.append(String.format("Start: %s\n", startIndex))
                .append(String.format("End: %s\n", endIndex));

        return visitGroup(pc, template, ctx.structureBlockBody());
    });
    }

    private StringBuilder visitGroup(PythonClass pc, PythonMember template, QEDocParser.StructureBlockBodyContext structureBlockBodyContext) {
        for (QEDocParser.BlockContext c: structureBlockBodyContext.block())
            if (c.plainTextBlock() != null) visit(c);


        for (QEDocParser.BlockContext c: structureBlockBodyContext.block()) {
            if (c.smartAssBlock() != null) {
                newMember(new PythonMember(template), pc);
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
            groupCounter++;
            newClass(new PythonClass(String.format("Group%d", groupCounter)), pc);

            for (QEDocParser.BlockContext c: ctx.structureBlockBody().block())
                if (c.plainTextBlock() != null)  visit(c);

            for (QEDocParser.BlockContext c: ctx.structureBlockBody().block())
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
        className.append(escape(programName));
        PythonClass pc = new PythonClass(className.toString());
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
    public StringBuilder visitNameListBlock(QEDocParser.NameListBlockContext ctx) { return withClass(pc -> {
            String className = ctx.structureBlockBody().ID().toString();

            newClass(new PythonClass(className), pc);
            super.visitNameListBlock(ctx);
            completeClass();

            newMember(new PythonMember(String.format("namelist_%s", className), className), pc);
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
            PythonClass optionClass = newClass(new PythonEnumClass(name), pc);
            pm.type = optionClass.name;

            for (QEDocParser.BlockContext c: ctx.structureBlockBody().block()) {
                if (c.plainTextBlock() != null) {
                    PythonMember npm = newMember(new PythonMember(), new PythonClass(""));
                    visit(c);
                    completeMember();
                    optionClass.others.append(npm.info);
                }
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
    public StringBuilder visitRowBlock(QEDocParser.RowBlockContext ctx) { return withClass(pc -> {
        String typeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
        newMember(new PythonMember(
                ctx.structureBlockBody().ID().toString(), translateType(typeName)), pc);
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
            PythonMember template = newMember(new PythonMember("",
                    translateType(escape(typeName != null ? typeName : "STRING"))),
                    new PythonClass(""));

            return visitGroup(pc, template, ctx);
        });
    }

    @Override
    public StringBuilder visitRowsBlock(QEDocParser.RowsBlockContext ctx) {
        withClass(pc -> {
            pc.name.append("_").append("row");
            for (TerminalNode t: ctx.structureBlockBody().SwitchText())
                pc.others.append(t.getText());
            return null;
        });
        return super.visitRowsBlock(ctx);

    }

    @Override
    public StringBuilder visitSectionBlock(QEDocParser.SectionBlockContext ctx) {
//        return super.visitSectionBlock(ctx);
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
    public StringBuilder visitTableBlock(QEDocParser.TableBlockContext ctx) { return withClass(pc -> {
        PythonClass tableClass = newClass(new PythonClass(ctx.structureBlockBody().ID().toString()), pc);
        super.visitTableBlock(ctx);
        completeClass();
        newMember(new PythonMember(ctx.Table().getText(),
                String.format("List[%s]", translateType(tableClass.name.toString()))), pc);
        completeMember();
        return null;
    });}

    private String getSwitch(TerminalNode text, String switchName) {
        Pattern varTypeBuilderSwitchRegex = Pattern.compile(
                String.format("-%s\\s+(.+)", switchName), Pattern.CASE_INSENSITIVE);
        Matcher m = varTypeBuilderSwitchRegex.matcher(text.toString());
        if (m.find()) { return m.group(1).trim(); }
        else { return null; }
    }
    private String getSwitch(List<TerminalNode> switches, String switchName) {
        for (TerminalNode text: switches) {
            String result = getSwitch(text, switchName);
            if (result != null) return result;
        }
        return null;
    }

    @Override
    public StringBuilder visitVarBlock(QEDocParser.VarBlockContext ctx) {
        withClass(pc -> {
            String typeName = getSwitch(ctx.structureBlockBody().SwitchText(), "type");
            newMember(new PythonMember(ctx.structureBlockBody().ID().toString(), translateType(typeName)), pc);
            return null;
        });
        super.visitVarBlock(ctx);
        return null;
    }

    @Override
    public StringBuilder visitVarGroupBlock(QEDocParser.VarGroupBlockContext ctx) {
        return visitRowOrColGroupBlock(ctx.structureBlockBody());
    }

    private String escape(String input) {

        return input.replace("\"", "")
                .replace("=", "_is_")
                .replace("'", "")
                .replace(".", "_")
                .replace("OR", "_or_")
                .replaceAll("\\s+", "_");
    }

    private StringBuilder visitConditional(QEDocParser.StructureBlockContext ctx,
                                  QEDocParser.StructureBlockBodyContext ctxBody,
                                  Function<QEDocParser.StructureBlockContext, StringBuilder> visit) {
        return withClass(pc -> {
            String predicate = getSwitch(ctxBody.SwitchText(), "test");
            PythonClass predicateClass = newClass(new PythonClass(String.format("%s_%s", pc.name,
                    escape(predicate != null ? predicate : "Otherwise"))), pc);
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
    public StringBuilder visitSmartColBlock(QEDocParser.SmartColBlockContext ctx) { return withMember(pm -> {
        pm.name = new StringBuilder(ctx.ID().getText());
        return null;
    });}

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
    public StringBuilder visitSmartDimBlock(QEDocParser.SmartDimBlockContext ctx) { return withMember(pm -> {
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
    public StringBuilder visitSmartRowBlock(QEDocParser.SmartRowBlockContext ctx) { return withMember(pm -> {
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
    public StringBuilder visitSmartVarBlock(QEDocParser.SmartVarBlockContext ctx) { return withMember(pm -> {
            pm.name = new StringBuilder(ctx.ID().getText());
            return null;
        });
    }

    @Override
    public StringBuilder visitSmartWhenBlock(QEDocParser.SmartWhenBlockContext ctx) {
        return super.visitSmartWhenBlock(ctx);
    }
}
