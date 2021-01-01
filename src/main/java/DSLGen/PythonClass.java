package DSLGen;

import java.util.ArrayList;

public class PythonClass {
    public StringBuilder name;
    public ArrayList<PythonMember> members;
    public ArrayList<PythonClass> imports;
    public boolean toc = false;
    public StringBuilder intro;
    public StringBuilder label;
    private ArrayList<PythonClass> inherits;
    public StringBuilder others;
    public StringBuilder message;

    public PythonClass(StringBuilder name) {
        this.name = name;
        members = new ArrayList<>();
        imports = new ArrayList<>();
        intro = new StringBuilder();
        label = new StringBuilder();
        inherits = new ArrayList<>();
        others = new StringBuilder();
        message = new StringBuilder();
    }

    public PythonClass(String text) {
        this(new StringBuilder(text));
    }

    public String toString() {
        StringBuilder builder = new StringBuilder(String.format("name: %s\n", name));
        builder.append("inherits:\n");
        for (PythonClass inherit: inherits) builder.append(String.format("%s\n", inherit.name).indent(4));
        builder.append("imports:\n");
        for (PythonClass i: imports) builder.append(String.format("%s\n", i.name).indent(4));
        builder.append("members:\n");
        for (PythonMember member: members) builder.append(String.format("%s: %s", member.name, member.type).indent(4));
        return builder.toString();
    }

    public void addInherit(PythonClass inherit) {
        inherits.add(inherit);
    }
}
