package DSLGen;

import GeneratedQEGrammar.QEDocLexer;
import GeneratedQEGrammar.QEDocParser;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Map;

public class QEDSLGenerator {


    public static void main(String[] args) throws IOException {
        String inputFile = null;
        if (args.length > 0) inputFile = args[0];
        InputStream is = System.in;
        if (inputFile != null) is = new FileInputStream(inputFile);
        CharStream input = CharStreams.fromStream(is);
        QEDocLexer lexer = new QEDocLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        QEDocParser parser = new QEDocParser(tokens);
        ParseTree tree = parser.def();
        DSLVisitor visitor = new DSLVisitor();
        visitor.visit(tree);
        File dir = new File(String.format(
                "/Users/kangbo/v_drive/creamer_doc_parser/generated_frontend/%s",
                new ClassPython(visitor.topLevelClass).getName()));
        if (!dir.exists()) {
            if (!dir.mkdir()) {
                System.err.printf("Cannot make directory: %s%n", dir.getAbsolutePath());
                return;
            }
        }
        else {
            System.out.printf("Directory already exists: %s%n", dir.getAbsolutePath());
        }
        String[] filenames = {"Card.py", "Choice.py", "Choose.py",
                "Group.py", "Namelist.py", "Options.py", "Row.py"};

        for (String filename: filenames) {
            Path source = Paths.get("src/main/resources/superClasses", filename);
            Path destination = Paths.get(dir.getAbsolutePath(), filename);
            Files.copy(source, destination, StandardCopyOption.REPLACE_EXISTING);
        }

        for (Map.Entry<String, ClassInternal> entry: visitor.pythonClasses.entrySet()) {
            ClassPython pc = new ClassPython(entry.getValue());
            File file = new File(String.format("%s/%s.py", dir.getAbsolutePath(), pc.getName()));
            file.createNewFile();
            FileWriter writer =  new FileWriter(file, false);
            pc.toPython(writer);
            writer.close();
        }
        File file = new File(String.format("%s/__init__.py", dir.getAbsolutePath()));

        if (!file.exists()) {
            if (!file.createNewFile()) {
                System.out.printf("Cannot make new file: %s%n", dir.getAbsolutePath());
                return;
            }
        }
        else {
            System.out.printf("File already exists: %s%n", dir.getAbsolutePath());
        }
        System.out.println(file.getAbsolutePath());
        FileWriter writer = new FileWriter(file);

        for (Map.Entry<String, ClassInternal> entry: visitor.pythonClasses.entrySet()) {
            ClassPython pc = new ClassPython(entry.getValue());
            writer.write(String.format("from .%s import %s\n",
                    pc.getName(), pc.getName()));
        }

        writer.write("__all__ = [");
        for (Map.Entry<String, ClassInternal> entry: visitor.pythonClasses.entrySet()) {
            ClassPython pc = new ClassPython(entry.getValue());
            writer.write(String.format("'%s', ", pc.getName()));
//            for (MemberInternal pm: pc.members) {
//                System.out.println(pm.defaultString.toString());
//            }
        }
        writer.write("]\n");
        writer.close();

    }

}
