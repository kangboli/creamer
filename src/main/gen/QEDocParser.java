// Generated from /home/telephant/Workspace/creamer_doc_parser/src/main/QEDocGrammar/QEDocParser.g4 by ANTLR 4.9
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class QEDocParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IntroBegin=1, DefaultBegin=2, InfoBegin=3, OptBegin=4, StatusBegin=5, 
		TOC=6, NameList=7, Var=8, VarGroup=9, InputDiscription=10, Flag=11, Scoped=12, 
		String=13, ID=14, WS=15, OB=16, CB=17, Ref=18, Bold=19, StringText=20, 
		LogicalText=21, ScopedText=22, WordText=23, EndText=24;
	public static final int
		RULE_def = 0, RULE_preamble = 1, RULE_preambleFlag = 2, RULE_block = 3, 
		RULE_intro = 4, RULE_nameList = 5, RULE_variable = 6, RULE_varSingle = 7, 
		RULE_varGroup = 8, RULE_variableDeclaration = 9, RULE_variableContent = 10, 
		RULE_default = 11, RULE_opts = 12, RULE_optContent = 13, RULE_info = 14, 
		RULE_opt = 15, RULE_status = 16, RULE_phrase = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"def", "preamble", "preambleFlag", "block", "intro", "nameList", "variable", 
			"varSingle", "varGroup", "variableDeclaration", "variableContent", "default", 
			"opts", "optContent", "info", "opt", "status", "phrase"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, "'namelist'", "'var'", "'vargroup'", 
			"'input_description'", null, null, null, null, null, "'{'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IntroBegin", "DefaultBegin", "InfoBegin", "OptBegin", "StatusBegin", 
			"TOC", "NameList", "Var", "VarGroup", "InputDiscription", "Flag", "Scoped", 
			"String", "ID", "WS", "OB", "CB", "Ref", "Bold", "StringText", "LogicalText", 
			"ScopedText", "WordText", "EndText"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "QEDocParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public QEDocParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class DefContext extends ParserRuleContext {
		public PreambleContext preamble() {
			return getRuleContext(PreambleContext.class,0);
		}
		public TerminalNode OB() { return getToken(QEDocParser.OB, 0); }
		public TerminalNode CB() { return getToken(QEDocParser.CB, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public DefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_def; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitDef(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitDef(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DefContext def() throws RecognitionException {
		DefContext _localctx = new DefContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_def);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			preamble();
			setState(37);
			match(OB);
			setState(39); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(38);
				block();
				}
				}
				setState(41); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntroBegin) | (1L << TOC) | (1L << NameList))) != 0) );
			setState(43);
			match(CB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreambleContext extends ParserRuleContext {
		public TerminalNode InputDiscription() { return getToken(QEDocParser.InputDiscription, 0); }
		public List<PreambleFlagContext> preambleFlag() {
			return getRuleContexts(PreambleFlagContext.class);
		}
		public PreambleFlagContext preambleFlag(int i) {
			return getRuleContext(PreambleFlagContext.class,i);
		}
		public PreambleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preamble; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterPreamble(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitPreamble(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitPreamble(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PreambleContext preamble() throws RecognitionException {
		PreambleContext _localctx = new PreambleContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_preamble);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(InputDiscription);
			setState(47); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(46);
				preambleFlag();
				}
				}
				setState(49); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Flag );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreambleFlagContext extends ParserRuleContext {
		public TerminalNode Flag() { return getToken(QEDocParser.Flag, 0); }
		public TerminalNode Scoped() { return getToken(QEDocParser.Scoped, 0); }
		public PreambleFlagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preambleFlag; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterPreambleFlag(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitPreambleFlag(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitPreambleFlag(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PreambleFlagContext preambleFlag() throws RecognitionException {
		PreambleFlagContext _localctx = new PreambleFlagContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_preambleFlag);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(Flag);
			setState(52);
			match(Scoped);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode TOC() { return getToken(QEDocParser.TOC, 0); }
		public IntroContext intro() {
			return getRuleContext(IntroContext.class,0);
		}
		public NameListContext nameList() {
			return getRuleContext(NameListContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_block);
		try {
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TOC:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				match(TOC);
				}
				break;
			case IntroBegin:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				intro();
				}
				break;
			case NameList:
				enterOuterAlt(_localctx, 3);
				{
				setState(56);
				nameList();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntroContext extends ParserRuleContext {
		public TerminalNode IntroBegin() { return getToken(QEDocParser.IntroBegin, 0); }
		public TerminalNode EndText() { return getToken(QEDocParser.EndText, 0); }
		public List<PhraseContext> phrase() {
			return getRuleContexts(PhraseContext.class);
		}
		public PhraseContext phrase(int i) {
			return getRuleContext(PhraseContext.class,i);
		}
		public IntroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intro; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterIntro(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitIntro(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitIntro(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IntroContext intro() throws RecognitionException {
		IntroContext _localctx = new IntroContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_intro);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(IntroBegin);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Ref) | (1L << Bold) | (1L << StringText) | (1L << LogicalText) | (1L << ScopedText) | (1L << WordText))) != 0)) {
				{
				{
				setState(60);
				phrase();
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(66);
			match(EndText);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NameListContext extends ParserRuleContext {
		public TerminalNode NameList() { return getToken(QEDocParser.NameList, 0); }
		public TerminalNode WordText() { return getToken(QEDocParser.WordText, 0); }
		public TerminalNode OB() { return getToken(QEDocParser.OB, 0); }
		public TerminalNode CB() { return getToken(QEDocParser.CB, 0); }
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public NameListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nameList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterNameList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitNameList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitNameList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NameListContext nameList() throws RecognitionException {
		NameListContext _localctx = new NameListContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_nameList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(NameList);
			setState(69);
			match(WordText);
			setState(70);
			match(OB);
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Var || _la==VarGroup) {
				{
				{
				setState(71);
				variable();
				}
				}
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(77);
			match(CB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public VarSingleContext varSingle() {
			return getRuleContext(VarSingleContext.class,0);
		}
		public VarGroupContext varGroup() {
			return getRuleContext(VarGroupContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitVariable(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitVariable(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_variable);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Var:
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				varSingle();
				}
				break;
			case VarGroup:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				varGroup();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarSingleContext extends ParserRuleContext {
		public TerminalNode Var() { return getToken(QEDocParser.Var, 0); }
		public List<TerminalNode> ID() { return getTokens(QEDocParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(QEDocParser.ID, i);
		}
		public TerminalNode Flag() { return getToken(QEDocParser.Flag, 0); }
		public TerminalNode OB() { return getToken(QEDocParser.OB, 0); }
		public TerminalNode CB() { return getToken(QEDocParser.CB, 0); }
		public List<VariableContentContext> variableContent() {
			return getRuleContexts(VariableContentContext.class);
		}
		public VariableContentContext variableContent(int i) {
			return getRuleContext(VariableContentContext.class,i);
		}
		public VarSingleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varSingle; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterVarSingle(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitVarSingle(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitVarSingle(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarSingleContext varSingle() throws RecognitionException {
		VarSingleContext _localctx = new VarSingleContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_varSingle);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(Var);
			setState(84);
			match(ID);
			setState(85);
			match(Flag);
			setState(86);
			match(ID);
			setState(87);
			match(OB);
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DefaultBegin) | (1L << InfoBegin) | (1L << OptBegin) | (1L << StatusBegin))) != 0)) {
				{
				{
				setState(88);
				variableContent();
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(94);
			match(CB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarGroupContext extends ParserRuleContext {
		public TerminalNode VarGroup() { return getToken(QEDocParser.VarGroup, 0); }
		public TerminalNode Flag() { return getToken(QEDocParser.Flag, 0); }
		public TerminalNode ID() { return getToken(QEDocParser.ID, 0); }
		public TerminalNode OB() { return getToken(QEDocParser.OB, 0); }
		public TerminalNode CB() { return getToken(QEDocParser.CB, 0); }
		public List<VariableDeclarationContext> variableDeclaration() {
			return getRuleContexts(VariableDeclarationContext.class);
		}
		public VariableDeclarationContext variableDeclaration(int i) {
			return getRuleContext(VariableDeclarationContext.class,i);
		}
		public List<VariableContentContext> variableContent() {
			return getRuleContexts(VariableContentContext.class);
		}
		public VariableContentContext variableContent(int i) {
			return getRuleContext(VariableContentContext.class,i);
		}
		public VarGroupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varGroup; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterVarGroup(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitVarGroup(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitVarGroup(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarGroupContext varGroup() throws RecognitionException {
		VarGroupContext _localctx = new VarGroupContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_varGroup);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(VarGroup);
			setState(97);
			match(Flag);
			setState(98);
			match(ID);
			setState(99);
			match(OB);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Var) {
				{
				{
				setState(100);
				variableDeclaration();
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DefaultBegin) | (1L << InfoBegin) | (1L << OptBegin) | (1L << StatusBegin))) != 0)) {
				{
				{
				setState(106);
				variableContent();
				}
				}
				setState(111);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(112);
			match(CB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclarationContext extends ParserRuleContext {
		public TerminalNode Var() { return getToken(QEDocParser.Var, 0); }
		public TerminalNode ID() { return getToken(QEDocParser.ID, 0); }
		public VariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterVariableDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitVariableDeclaration(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitVariableDeclaration(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VariableDeclarationContext variableDeclaration() throws RecognitionException {
		VariableDeclarationContext _localctx = new VariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_variableDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(Var);
			setState(115);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContentContext extends ParserRuleContext {
		public DefaultContext default() {
			return getRuleContext(DefaultContext.class,0);
		}
		public InfoContext info() {
			return getRuleContext(InfoContext.class,0);
		}
		public StatusContext status() {
			return getRuleContext(StatusContext.class,0);
		}
		public OptsContext opts() {
			return getRuleContext(OptsContext.class,0);
		}
		public VariableContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableContent; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterVariableContent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitVariableContent(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitVariableContent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VariableContentContext variableContent() throws RecognitionException {
		VariableContentContext _localctx = new VariableContentContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_variableContent);
		try {
			setState(121);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(117);
				default();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				info();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(119);
				status();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(120);
				opts();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefaultContext extends ParserRuleContext {
		public TerminalNode DefaultBegin() { return getToken(QEDocParser.DefaultBegin, 0); }
		public TerminalNode EndText() { return getToken(QEDocParser.EndText, 0); }
		public List<PhraseContext> phrase() {
			return getRuleContexts(PhraseContext.class);
		}
		public PhraseContext phrase(int i) {
			return getRuleContext(PhraseContext.class,i);
		}
		public DefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_default; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterDefault(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitDefault(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitDefault(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DefaultContext default() throws RecognitionException {
		DefaultContext _localctx = new DefaultContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_default);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(DefaultBegin);
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Ref) | (1L << Bold) | (1L << StringText) | (1L << LogicalText) | (1L << ScopedText) | (1L << WordText))) != 0)) {
				{
				{
				setState(124);
				phrase();
				}
				}
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(130);
			match(EndText);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OptsContext extends ParserRuleContext {
		public List<OptContentContext> optContent() {
			return getRuleContexts(OptContentContext.class);
		}
		public OptContentContext optContent(int i) {
			return getRuleContext(OptContentContext.class,i);
		}
		public OptsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opts; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterOpts(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitOpts(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitOpts(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OptsContext opts() throws RecognitionException {
		OptsContext _localctx = new OptsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_opts);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(133); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(132);
					optContent();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(135); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OptContentContext extends ParserRuleContext {
		public OptContext opt() {
			return getRuleContext(OptContext.class,0);
		}
		public InfoContext info() {
			return getRuleContext(InfoContext.class,0);
		}
		public OptContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optContent; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterOptContent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitOptContent(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitOptContent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OptContentContext optContent() throws RecognitionException {
		OptContentContext _localctx = new OptContentContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_optContent);
		try {
			setState(139);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OptBegin:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				opt();
				}
				break;
			case InfoBegin:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				info();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InfoContext extends ParserRuleContext {
		public TerminalNode InfoBegin() { return getToken(QEDocParser.InfoBegin, 0); }
		public TerminalNode EndText() { return getToken(QEDocParser.EndText, 0); }
		public List<PhraseContext> phrase() {
			return getRuleContexts(PhraseContext.class);
		}
		public PhraseContext phrase(int i) {
			return getRuleContext(PhraseContext.class,i);
		}
		public InfoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_info; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterInfo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitInfo(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitInfo(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InfoContext info() throws RecognitionException {
		InfoContext _localctx = new InfoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_info);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(InfoBegin);
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Ref) | (1L << Bold) | (1L << StringText) | (1L << LogicalText) | (1L << ScopedText) | (1L << WordText))) != 0)) {
				{
				{
				setState(142);
				phrase();
				}
				}
				setState(147);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(148);
			match(EndText);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OptContext extends ParserRuleContext {
		public TerminalNode OptBegin() { return getToken(QEDocParser.OptBegin, 0); }
		public TerminalNode EndText() { return getToken(QEDocParser.EndText, 0); }
		public List<PhraseContext> phrase() {
			return getRuleContexts(PhraseContext.class);
		}
		public PhraseContext phrase(int i) {
			return getRuleContext(PhraseContext.class,i);
		}
		public OptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterOpt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitOpt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitOpt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OptContext opt() throws RecognitionException {
		OptContext _localctx = new OptContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_opt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(OptBegin);
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Ref) | (1L << Bold) | (1L << StringText) | (1L << LogicalText) | (1L << ScopedText) | (1L << WordText))) != 0)) {
				{
				{
				setState(151);
				phrase();
				}
				}
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(157);
			match(EndText);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatusContext extends ParserRuleContext {
		public TerminalNode StatusBegin() { return getToken(QEDocParser.StatusBegin, 0); }
		public TerminalNode EndText() { return getToken(QEDocParser.EndText, 0); }
		public List<PhraseContext> phrase() {
			return getRuleContexts(PhraseContext.class);
		}
		public PhraseContext phrase(int i) {
			return getRuleContext(PhraseContext.class,i);
		}
		public StatusContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_status; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterStatus(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitStatus(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitStatus(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatusContext status() throws RecognitionException {
		StatusContext _localctx = new StatusContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_status);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(StatusBegin);
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Ref) | (1L << Bold) | (1L << StringText) | (1L << LogicalText) | (1L << ScopedText) | (1L << WordText))) != 0)) {
				{
				{
				setState(160);
				phrase();
				}
				}
				setState(165);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(166);
			match(EndText);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PhraseContext extends ParserRuleContext {
		public TerminalNode Ref() { return getToken(QEDocParser.Ref, 0); }
		public TerminalNode Bold() { return getToken(QEDocParser.Bold, 0); }
		public TerminalNode StringText() { return getToken(QEDocParser.StringText, 0); }
		public TerminalNode LogicalText() { return getToken(QEDocParser.LogicalText, 0); }
		public TerminalNode ScopedText() { return getToken(QEDocParser.ScopedText, 0); }
		public TerminalNode WordText() { return getToken(QEDocParser.WordText, 0); }
		public PhraseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_phrase; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).enterPhrase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof QEDocParserListener ) ((QEDocParserListener)listener).exitPhrase(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof QEDocParserVisitor ) return ((QEDocParserVisitor<? extends T>)visitor).visitPhrase(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PhraseContext phrase() throws RecognitionException {
		PhraseContext _localctx = new PhraseContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_phrase);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Ref) | (1L << Bold) | (1L << StringText) | (1L << LogicalText) | (1L << ScopedText) | (1L << WordText))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32\u00ad\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\2\6\2*\n\2\r\2\16\2+\3\2\3\2\3\3\3\3\6\3\62\n\3\r"+
		"\3\16\3\63\3\4\3\4\3\4\3\5\3\5\3\5\5\5<\n\5\3\6\3\6\7\6@\n\6\f\6\16\6"+
		"C\13\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7K\n\7\f\7\16\7N\13\7\3\7\3\7\3\b\3\b"+
		"\5\bT\n\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\\\n\t\f\t\16\t_\13\t\3\t\3\t\3\n"+
		"\3\n\3\n\3\n\3\n\7\nh\n\n\f\n\16\nk\13\n\3\n\7\nn\n\n\f\n\16\nq\13\n\3"+
		"\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f|\n\f\3\r\3\r\7\r\u0080\n\r\f"+
		"\r\16\r\u0083\13\r\3\r\3\r\3\16\6\16\u0088\n\16\r\16\16\16\u0089\3\17"+
		"\3\17\5\17\u008e\n\17\3\20\3\20\7\20\u0092\n\20\f\20\16\20\u0095\13\20"+
		"\3\20\3\20\3\21\3\21\7\21\u009b\n\21\f\21\16\21\u009e\13\21\3\21\3\21"+
		"\3\22\3\22\7\22\u00a4\n\22\f\22\16\22\u00a7\13\22\3\22\3\22\3\23\3\23"+
		"\3\23\2\2\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\3\3\2\24\31"+
		"\2\u00ad\2&\3\2\2\2\4/\3\2\2\2\6\65\3\2\2\2\b;\3\2\2\2\n=\3\2\2\2\fF\3"+
		"\2\2\2\16S\3\2\2\2\20U\3\2\2\2\22b\3\2\2\2\24t\3\2\2\2\26{\3\2\2\2\30"+
		"}\3\2\2\2\32\u0087\3\2\2\2\34\u008d\3\2\2\2\36\u008f\3\2\2\2 \u0098\3"+
		"\2\2\2\"\u00a1\3\2\2\2$\u00aa\3\2\2\2&\'\5\4\3\2\')\7\22\2\2(*\5\b\5\2"+
		")(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,-\3\2\2\2-.\7\23\2\2.\3\3\2\2"+
		"\2/\61\7\f\2\2\60\62\5\6\4\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2"+
		"\63\64\3\2\2\2\64\5\3\2\2\2\65\66\7\r\2\2\66\67\7\16\2\2\67\7\3\2\2\2"+
		"8<\7\b\2\29<\5\n\6\2:<\5\f\7\2;8\3\2\2\2;9\3\2\2\2;:\3\2\2\2<\t\3\2\2"+
		"\2=A\7\3\2\2>@\5$\23\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2"+
		"\2CA\3\2\2\2DE\7\32\2\2E\13\3\2\2\2FG\7\t\2\2GH\7\31\2\2HL\7\22\2\2IK"+
		"\5\16\b\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2"+
		"OP\7\23\2\2P\r\3\2\2\2QT\5\20\t\2RT\5\22\n\2SQ\3\2\2\2SR\3\2\2\2T\17\3"+
		"\2\2\2UV\7\n\2\2VW\7\20\2\2WX\7\r\2\2XY\7\20\2\2Y]\7\22\2\2Z\\\5\26\f"+
		"\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7\23"+
		"\2\2a\21\3\2\2\2bc\7\13\2\2cd\7\r\2\2de\7\20\2\2ei\7\22\2\2fh\5\24\13"+
		"\2gf\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jo\3\2\2\2ki\3\2\2\2ln\5\26"+
		"\f\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2pr\3\2\2\2qo\3\2\2\2rs\7\23"+
		"\2\2s\23\3\2\2\2tu\7\n\2\2uv\7\20\2\2v\25\3\2\2\2w|\5\30\r\2x|\5\36\20"+
		"\2y|\5\"\22\2z|\5\32\16\2{w\3\2\2\2{x\3\2\2\2{y\3\2\2\2{z\3\2\2\2|\27"+
		"\3\2\2\2}\u0081\7\4\2\2~\u0080\5$\23\2\177~\3\2\2\2\u0080\u0083\3\2\2"+
		"\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081"+
		"\3\2\2\2\u0084\u0085\7\32\2\2\u0085\31\3\2\2\2\u0086\u0088\5\34\17\2\u0087"+
		"\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2"+
		"\2\2\u008a\33\3\2\2\2\u008b\u008e\5 \21\2\u008c\u008e\5\36\20\2\u008d"+
		"\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\35\3\2\2\2\u008f\u0093\7\5\2"+
		"\2\u0090\u0092\5$\23\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091"+
		"\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096"+
		"\u0097\7\32\2\2\u0097\37\3\2\2\2\u0098\u009c\7\6\2\2\u0099\u009b\5$\23"+
		"\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d"+
		"\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\7\32\2\2"+
		"\u00a0!\3\2\2\2\u00a1\u00a5\7\7\2\2\u00a2\u00a4\5$\23\2\u00a3\u00a2\3"+
		"\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6"+
		"\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7\32\2\2\u00a9#\3\2\2\2"+
		"\u00aa\u00ab\t\2\2\2\u00ab%\3\2\2\2\22+\63;ALS]io{\u0081\u0089\u008d\u0093"+
		"\u009c\u00a5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}