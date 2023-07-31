package DSLGen;


import java.util.Locale;

public class MemberPython extends MemberInternal{
    MemberPython(MemberInternal internal) {
        super(internal);
    }

    public boolean isBuiltin() {
        return isBuiltin(super.getType());
    }
    public boolean hasDoc() {
        return !getInfo().equals("") || !getDefaultString().equals("") || !others.toString().equals("");
    }

    public static boolean isBuiltin(String type) {
        String[] builtinTypes = {"CHARACTER", "STRING", "INTEGER", "REAL", "LOGICAL"};
        for (String t: builtinTypes) {
            if (type.toUpperCase().contains(t)) return true;
        }
        return false;
    }

    public String getName() {
        return ClassInternal.escape(super.getName());
    }

    public String getType() {
        String typeName;
        boolean isList = super.getType().contains("List");
        if (isList) { typeName = super.getType().split(" ")[1]; }
        else typeName = super.getType().trim();

//        System.out.println(typeName);
        if (isBuiltin(typeName)) {
            if (isList) return String.format("List[%s]",
                    ClassInternal.translateType(typeName));
            else return ClassInternal.translateType(super.getType());
        } else {
            if (isList) return String.format("List[%s]",
                    ClassPython.convertName(ClassInternal.translateType(typeName)));
            else return ClassPython.convertName(ClassInternal.translateType(super.getType()));
        }
    }

    public String getInfo () {
        return super.getInfo().indent(8);
    }

    public static String indent(String input) {
        return input.indent(4);
    }

    public String getDefault() {
        return getDefaultString().indent(8);
    }

    public String getOthers() {
        return others.toString().indent(8);
    }

}
