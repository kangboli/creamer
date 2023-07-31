package DSLGen;

import freemarker.template.Template;
import freemarker.template.TemplateException;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class ClassPython extends ClassInternal{

    public ClassPython(String name) {
        super(name);
    }

    public ClassPython(ClassInternal internal) {
        super(internal);
    }

    public ArrayList<ClassPython> getImports() {
        return imports.stream().map(ClassPython::new)
                .collect(Collectors.toCollection(ArrayList::new));
    }

    public ArrayList<ClassPython> getInherits() {
        return inherits.stream().map(ClassPython::new)
                .collect(Collectors.toCollection(ArrayList::new));
    }

    public String getCommaSeparatedInherits() {
        ArrayList<String> inheritNames = new ArrayList<>();
        for (ClassInternal pc:  inherits) {
            inheritNames.add(new ClassPython(pc).getName());
        }
        return String.join(", ", inheritNames);
    }

    public HashMap<String, String> getEnums() {
        HashMap<String, String> formattedEnum = new HashMap<>();
        for (Map.Entry<String, StringBuilder> entry: enums.entrySet()) {
            formattedEnum.put(escape(entry.getKey()).toLowerCase(),
                    entry.getValue().toString().indent(3));
        }
        return formattedEnum;
    }

    public String getName() {
        return convertName(super.getName());
    }

    public static String convertName(String name) {
        StringBuilder builder = new StringBuilder();
        for (String word: escape(name).split("_+"))
            if (word.length() > 0) builder.append(word.substring(0, 1)
                    .toUpperCase()).append(word.substring(1).toLowerCase());
        return builder.toString();

    }

    public ArrayList<MemberPython> getMembers() {
        return members.stream().map(MemberPython::new).collect(Collectors.toCollection(ArrayList::new));
    }

    public String getIntro() {
        return intro.toString().indent(4);
    }

    public String getLabel() {
        return label.toString().indent(4);
    }

    public String getMessage() {
        return message.toString().indent(4);
    }

    public String getOthers() {
        return others.toString().indent(4);
    }

    public boolean hasDoc() {
        return !intro.toString().equals("") || !label.toString().equals("") || !others.toString().equals("") || !message.toString().equals("");
    }

    public void toPython(OutputStreamWriter stream) {
        HashMap<String, Object> root = new HashMap<>();
//        for (ClassInternal pc: imports) System.out.println(pc.name.toString());
//        System.out.println(name);
        root.put("pc", this);
        try {
            configureTemplate();
            Template temp = cfg.getTemplate("pythonClass");
            temp.process(root, stream);
        } catch (IOException | TemplateException e) { e.printStackTrace(); }
    }

}
