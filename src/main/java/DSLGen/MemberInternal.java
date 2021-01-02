package DSLGen;

public class MemberInternal {
    protected StringBuilder name;
    public StringBuilder type;
    public StringBuilder info;
    public StringBuilder defaultString;
    public StringBuilder others;

    public MemberInternal(String name, String type) {
        this.name = new StringBuilder(name);
        this.type = new StringBuilder(type);
        info = new StringBuilder();
        defaultString = new StringBuilder();
        others = new StringBuilder();
    }

    public MemberInternal(MemberInternal another) {
        name = new StringBuilder(another.name);
        type = new StringBuilder(another.type);
        info = new StringBuilder(another.info);
        defaultString = new StringBuilder(another.defaultString);
        others = new StringBuilder(another.others);
    }

    public String toString() {
        return String.format("name: %s\n", name) +
                String.format("type: %s\n", type) +
                String.format("info: %s\n", info) +
                String.format("default: %s\n", defaultString);
    }
}
