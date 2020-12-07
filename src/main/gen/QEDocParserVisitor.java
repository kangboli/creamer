// Generated from /home/telephant/Workspace/creamer_doc_parser/src/main/QEDocGrammar/QEDocParser.g4 by ANTLR 4.9
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link QEDocParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface QEDocParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link QEDocParser#def}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDef(QEDocParser.DefContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#preamble}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPreamble(QEDocParser.PreambleContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#preambleFlag}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPreambleFlag(QEDocParser.PreambleFlagContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(QEDocParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#intro}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntro(QEDocParser.IntroContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#nameList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNameList(QEDocParser.NameListContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable(QEDocParser.VariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#varSingle}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarSingle(QEDocParser.VarSingleContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#varGroup}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarGroup(QEDocParser.VarGroupContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#variableDeclaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableDeclaration(QEDocParser.VariableDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#variableContent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableContent(QEDocParser.VariableContentContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#default}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefault(QEDocParser.DefaultContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#opts}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOpts(QEDocParser.OptsContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#optContent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOptContent(QEDocParser.OptContentContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#info}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInfo(QEDocParser.InfoContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#opt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOpt(QEDocParser.OptContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#status}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatus(QEDocParser.StatusContext ctx);
	/**
	 * Visit a parse tree produced by {@link QEDocParser#phrase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPhrase(QEDocParser.PhraseContext ctx);
}