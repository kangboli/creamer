package DSLGen;

public class MemberInternal {
    /*
     * This models a member/field of a ClassInternal.
     * The type of the member can be an elementary type or a ClassInternal.
     */
    private StringBuilder name;
    private StringBuilder type;
    private ClassInternal definedType;
    private final StringBuilder info;
    private final StringBuilder defaultString;
    public StringBuilder others;

    public MemberInternal(String name, String type) {
        this.name = name == null? null: new StringBuilder(name);
        this.type = type == null? null: new StringBuilder(type);
        info = new StringBuilder();
        defaultString = new StringBuilder();
        others = new StringBuilder();
    }

    public MemberInternal(MemberInternal another) {
        name = another.name == null? null: new StringBuilder(another.name);
        type = another.type == null? null: new StringBuilder(another.type);
        definedType = another.definedType;
        info = new StringBuilder(another.info);
        defaultString = new StringBuilder(another.getDefaultString());
        others = new StringBuilder(another.others);
    }

    public void setDefinedType(ClassInternal definedType) {
        this.definedType = definedType;
//        if (this.definedType == null) this.definedType = definedType;
//        else {
//            System.err.printf("%s -> %s%n", this.definedType.getName(), definedType.getName());
//            System.err.println("Defined type can only be set once.");
//        }
    }

    public ClassInternal getDefinedType(){
        return definedType;
    }

    public boolean isEnum() {
        return definedType != null && !definedType.enums.isEmpty();
    }

    public String getType() {
        if (definedType != null) return definedType.getName();
        else if (type == null) return null;
        else return type.toString();
    }

    public void setType(String type) {
        if (this.type == null) this.type = new StringBuilder(type);
        else {
            System.err.printf("%s -> %s%n", this.type.toString(), type);
            System.err.println("Type can only be set once.");
        }
    }

    public String getName() {
        if (name == null) return null;
        else return name.toString();
    }

    public void setName(String name) {
        if (this.name == null) this.name = new StringBuilder(name);
        else {
            System.err.printf("%s -> %s%n", this.name.toString(), name);
            System.err.println("The name of a member can only be set once.");
        }
    }

    public String getDefaultString() {
        return defaultString.toString();
    }

    public StringBuilder appendToDefaultString(String append) {
        defaultString.append(append);
        return new StringBuilder(defaultString.toString());
    }

    public String getInfo() {
        return info.toString();
    }

    public StringBuilder appendToInfo(String append) {
        info.append(append);
        return new StringBuilder(info.toString());
    }

    public String toString() {
        return String.format("name: %s\n", name) +
                String.format("type: %s\n", type) +
                String.format("info: %s\n", info) +
                String.format("default: %s\n", defaultString);
    }
}
