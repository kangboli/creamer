package DSLGen;


public class MemberPython extends MemberInternal{
    MemberPython(MemberInternal internal) {
        super(internal);
    }

    public boolean isBuiltin() {
        return isBuiltin(type.toString());
    }

    public static boolean isBuiltin(String type) {
        String[] builtinTypes = {"CHARACTER", "STRING", "INTEGER", "REAL", "LOGICAL"};
        for (String t: builtinTypes) {
            if (t.toUpperCase().equals(type)) return true;
        }
        return false;
    }

    public String getName() {
        return ClassInternal.escape(name.toString());
    }

    public String getType() {
        String typeName;
        boolean isList = type.toString().contains("List");
        if (isList) { typeName = type.toString().split(" ")[1]; }
        else typeName = type.toString().trim();

//        System.out.println(typeName);
        if (isBuiltin(typeName)) {
            if (isList) return String.format("List[%s]",
                    ClassInternal.translateType(typeName));
            else return ClassInternal.translateType(type.toString());
        } else {
            if (isList) return String.format("List[%s]",
                    ClassPython.convertName(ClassInternal.translateType(typeName)));
            else return ClassPython.convertName(ClassInternal.translateType(type.toString()));
        }
    }

    public String getInfo () {
        return info.toString();
    }

    public String getDefault() {
        return defaultString.toString();
    }

    public String getOthers() {
        return others.toString();
    }

}
