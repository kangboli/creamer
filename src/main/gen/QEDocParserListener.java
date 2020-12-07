// Generated from /home/telephant/Workspace/creamer_doc_parser/src/main/QEDocGrammar/QEDocParser.g4 by ANTLR 4.9
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link QEDocParser}.
 */
public interface QEDocParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link QEDocParser#def}.
	 * @param ctx the parse tree
	 */
	void enterDef(QEDocParser.DefContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#def}.
	 * @param ctx the parse tree
	 */
	void exitDef(QEDocParser.DefContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#preamble}.
	 * @param ctx the parse tree
	 */
	void enterPreamble(QEDocParser.PreambleContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#preamble}.
	 * @param ctx the parse tree
	 */
	void exitPreamble(QEDocParser.PreambleContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#preambleFlag}.
	 * @param ctx the parse tree
	 */
	void enterPreambleFlag(QEDocParser.PreambleFlagContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#preambleFlag}.
	 * @param ctx the parse tree
	 */
	void exitPreambleFlag(QEDocParser.PreambleFlagContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(QEDocParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(QEDocParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#intro}.
	 * @param ctx the parse tree
	 */
	void enterIntro(QEDocParser.IntroContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#intro}.
	 * @param ctx the parse tree
	 */
	void exitIntro(QEDocParser.IntroContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#nameList}.
	 * @param ctx the parse tree
	 */
	void enterNameList(QEDocParser.NameListContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#nameList}.
	 * @param ctx the parse tree
	 */
	void exitNameList(QEDocParser.NameListContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(QEDocParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(QEDocParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#varSingle}.
	 * @param ctx the parse tree
	 */
	void enterVarSingle(QEDocParser.VarSingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#varSingle}.
	 * @param ctx the parse tree
	 */
	void exitVarSingle(QEDocParser.VarSingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#varGroup}.
	 * @param ctx the parse tree
	 */
	void enterVarGroup(QEDocParser.VarGroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#varGroup}.
	 * @param ctx the parse tree
	 */
	void exitVarGroup(QEDocParser.VarGroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclaration(QEDocParser.VariableDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclaration(QEDocParser.VariableDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#variableContent}.
	 * @param ctx the parse tree
	 */
	void enterVariableContent(QEDocParser.VariableContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#variableContent}.
	 * @param ctx the parse tree
	 */
	void exitVariableContent(QEDocParser.VariableContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#default}.
	 * @param ctx the parse tree
	 */
	void enterDefault(QEDocParser.DefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#default}.
	 * @param ctx the parse tree
	 */
	void exitDefault(QEDocParser.DefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#opts}.
	 * @param ctx the parse tree
	 */
	void enterOpts(QEDocParser.OptsContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#opts}.
	 * @param ctx the parse tree
	 */
	void exitOpts(QEDocParser.OptsContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#optContent}.
	 * @param ctx the parse tree
	 */
	void enterOptContent(QEDocParser.OptContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#optContent}.
	 * @param ctx the parse tree
	 */
	void exitOptContent(QEDocParser.OptContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#info}.
	 * @param ctx the parse tree
	 */
	void enterInfo(QEDocParser.InfoContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#info}.
	 * @param ctx the parse tree
	 */
	void exitInfo(QEDocParser.InfoContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#opt}.
	 * @param ctx the parse tree
	 */
	void enterOpt(QEDocParser.OptContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#opt}.
	 * @param ctx the parse tree
	 */
	void exitOpt(QEDocParser.OptContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#status}.
	 * @param ctx the parse tree
	 */
	void enterStatus(QEDocParser.StatusContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#status}.
	 * @param ctx the parse tree
	 */
	void exitStatus(QEDocParser.StatusContext ctx);
	/**
	 * Enter a parse tree produced by {@link QEDocParser#phrase}.
	 * @param ctx the parse tree
	 */
	void enterPhrase(QEDocParser.PhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link QEDocParser#phrase}.
	 * @param ctx the parse tree
	 */
	void exitPhrase(QEDocParser.PhraseContext ctx);
}