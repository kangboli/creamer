package DSLGen;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class PythonEnumClass extends PythonClass {
    public HashMap<String, StringBuilder> enums;

    public PythonEnumClass(String name) {
        this(new StringBuilder(name));
    }

    public PythonEnumClass(StringBuilder name) {
        super(name);
        enums = new HashMap<>();
    }

    public String toString() {
        StringBuilder builder = new StringBuilder(super.toString());
        builder.append("enums:\n");
        for (Map.Entry<String, StringBuilder> e: enums.entrySet()) {
            builder.append(String.format("%s: %s\n", e.getKey(), e.getValue()).indent(4));
        }
        return builder.toString();
    }
}
