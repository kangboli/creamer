package DSLGen;

import GeneratedQEGrammar.QEDocLexer;
import GeneratedQEGrammar.QEDocParser;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

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
        DSLVisitor visitor = new DSLVisitor("/home/telephant/Workspace/creamer_doc_parser/generated_frontend");
        visitor.visit(tree);
        System.out.println(visitor.toString());
    }
}
