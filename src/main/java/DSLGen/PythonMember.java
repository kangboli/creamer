package DSLGen;

public class PythonMember {
    public StringBuilder name;
    public StringBuilder type;
    public StringBuilder info;
    public StringBuilder defaultString;
    public StringBuilder others;

    public PythonMember() {
        info = new StringBuilder();
        defaultString = new StringBuilder();
        others = new StringBuilder();
    }

    public PythonMember(String name, String type) {
        this();
        this.name = new StringBuilder(name);
        this.type = new StringBuilder(type);
    }

    public PythonMember(PythonMember another) {
        name = another.name;
        type = another.type;
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
