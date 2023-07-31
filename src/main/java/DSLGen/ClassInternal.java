package DSLGen;

import freemarker.core.PlainTextOutputFormat;
import freemarker.template.Configuration;
import freemarker.template.TemplateExceptionHandler;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ClassInternal {
    private StringBuilder name;
    public ArrayList<MemberInternal> members;
    public ArrayList<ClassInternal> imports;
    public boolean toc = false;
    public StringBuilder intro;
    public StringBuilder label;
    protected ArrayList<ClassInternal> inherits;
    public StringBuilder others;
    public StringBuilder message;
    public HashMap<String, StringBuilder> enums;
    protected Configuration cfg;

    public ClassInternal(String text) {
        this.name = new StringBuilder(text);
        members = new ArrayList<>();
        imports = new ArrayList<>();
        intro = new StringBuilder();
        label = new StringBuilder();
        inherits = new ArrayList<>();
        others = new StringBuilder();
        message = new StringBuilder();
        enums = new HashMap<>();
    }

    public ClassInternal(ClassInternal another) {
        this(another.name.toString());
        members = new ArrayList<>(another.members);
        imports = new ArrayList<>(another.imports);
        intro = new StringBuilder(another.intro);
        label = new StringBuilder(another.label);
        inherits = new ArrayList<>(another.inherits);
        others = new StringBuilder(another.others);
        message = new StringBuilder(another.message);
        enums = new HashMap<>(another.enums);
        toc = another.toc;
        cfg = another.cfg;
    }

    public String getName(){
        return name.toString();
    }

    public static String escape(String input) {
        return input.replace("\"", "")
                .replace("=", "__is__")
                .replace("'", "")
                .replace("{", "")
                .replace("}", "")
                .replace(",", "__comma__")
                .replace(".", "__dot__")
                .replace("-", "__dash__")
                .replace("(", "__lp__")
                .replace(")", "__rp__")
                .replace("lambda", "lambda_is_a_python_keyword")
                .replaceAll("\\s+", "__ws__");
    }

    protected static String translateType(String type) {
        return switch (type) {
            case "REAL" -> "float";
            case "INTEGER" -> "int";
            case "LOGICAL" -> "bool";
            case "CHARACTER", "STRING" -> "str";
            default -> type;
        };
    }

    public String toString() {
        StringBuilder builder = new StringBuilder(String.format("name: %s\n", name));
        builder.append("inherits:\n");
        for (ClassInternal inherit: inherits) builder.append(String.format("%s\n", inherit.name).indent(4));
        builder.append("imports:\n");
        for (ClassInternal i: imports) builder.append(String.format("%s\n", i.name).indent(4));
        builder.append("members:\n");
        for (MemberInternal member: members) builder.append(String.format("%s: %s", member.getName(), member.getType()).indent(4));
        builder.append("enums:\n");
        for (Map.Entry<String, StringBuilder> e: enums.entrySet()) {
            builder.append(String.format("%s: %s\n", e.getKey(), e.getValue()).indent(4));
        }
        return builder.toString();
    }

    public void addInherit(ClassInternal inherit) {
        inherits.add(inherit);
        imports.add(inherit);
    }

    protected void configureTemplate() throws IOException{
        cfg = new Configuration(Configuration.VERSION_2_3_29);
        cfg.setDirectoryForTemplateLoading(new File(
                "src/main/resources/frontendTemplates"));
        cfg.setDefaultEncoding("UTF-8");
        cfg.setTemplateExceptionHandler(TemplateExceptionHandler.RETHROW_HANDLER);
        cfg.setLogTemplateExceptions(false);
        cfg.setWrapUncheckedExceptions(true);
        cfg.setFallbackOnNullLoopVariable(false);
        cfg.setWhitespaceStripping(true);
        cfg.setOutputFormat(PlainTextOutputFormat.INSTANCE);
    }

}
