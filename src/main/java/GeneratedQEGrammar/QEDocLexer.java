// Generated from QEDocLexer.g4 by ANTLR 4.9
package GeneratedQEGrammar;
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class QEDocLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IntroBegin=1, DefaultBegin=2, InfoBegin=3, OptBegin=4, StatusBegin=5, 
		TOC=6, NameList=7, Var=8, VarGroup=9, InputDiscription=10, Flag=11, ID=12, 
		WS=13, OB=14, CB=15, Ref=16, Bold=17, String=18, Logical=19, Scoped=20, 
		Word=21, EndText=22;
	public static final int
		richText=1;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "richText"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"IntroBegin", "DefaultBegin", "InfoBegin", "OptBegin", "StatusBegin", 
			"TOC", "NameList", "Var", "VarGroup", "InputDiscription", "Flag", "ID", 
			"WS", "OB", "CB", "Ref", "Bold", "String", "Logical", "Scoped", "Word", 
			"EndText"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, "'namelist'", "'var'", "'vargroup'", 
			"'input_discription'", null, null, null, "'{'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IntroBegin", "DefaultBegin", "InfoBegin", "OptBegin", "StatusBegin", 
			"TOC", "NameList", "Var", "VarGroup", "InputDiscription", "Flag", "ID", 
			"WS", "OB", "CB", "Ref", "Bold", "String", "Logical", "Scoped", "Word", 
			"EndText"
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


	public QEDocLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "QEDocLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30\u00ea\b\1\b\1"+
		"\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t"+
		"\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4"+
		"\22\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5^\n\5\f\5\16\5a\13\5\3\5\3\5\5\5e\n\5"+
		"\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3"+
		"\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3"+
		"\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00bf\n\22\3\23\3\23"+
		"\7\23\u00c3\n\23\f\23\16\23\u00c6\13\23\3\23\3\23\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00d7\n\24\3\25\3\25"+
		"\7\25\u00db\n\25\f\25\16\25\u00de\13\25\3\25\3\25\3\26\6\26\u00e3\n\26"+
		"\r\26\16\26\u00e4\3\27\3\27\3\27\3\27\2\2\30\4\3\6\4\b\5\n\6\f\7\16\b"+
		"\20\t\22\n\24\13\26\f\30\r\32\16\34\17\36\20 \21\"\22$\23&\24(\25*\26"+
		",\27.\30\4\2\3\5\7\2\60\60\63;C\\aac|\5\2\13\f\17\17\"\"\7\2\13\f\17\17"+
		"\"\"}}\177\177\2\u00ef\2\4\3\2\2\2\2\6\3\2\2\2\2\b\3\2\2\2\2\n\3\2\2\2"+
		"\2\f\3\2\2\2\2\16\3\2\2\2\2\20\3\2\2\2\2\22\3\2\2\2\2\24\3\2\2\2\2\26"+
		"\3\2\2\2\2\30\3\2\2\2\2\32\3\2\2\2\2\34\3\2\2\2\2\36\3\2\2\2\2 \3\2\2"+
		"\2\3\"\3\2\2\2\3$\3\2\2\2\3&\3\2\2\2\3(\3\2\2\2\3*\3\2\2\2\3,\3\2\2\2"+
		"\3.\3\2\2\2\4\60\3\2\2\2\6:\3\2\2\2\bF\3\2\2\2\nO\3\2\2\2\fh\3\2\2\2\16"+
		"s\3\2\2\2\20z\3\2\2\2\22\u0083\3\2\2\2\24\u0087\3\2\2\2\26\u0090\3\2\2"+
		"\2\30\u00a2\3\2\2\2\32\u00a5\3\2\2\2\34\u00a7\3\2\2\2\36\u00ab\3\2\2\2"+
		" \u00ad\3\2\2\2\"\u00af\3\2\2\2$\u00be\3\2\2\2&\u00c0\3\2\2\2(\u00d6\3"+
		"\2\2\2*\u00d8\3\2\2\2,\u00e2\3\2\2\2.\u00e6\3\2\2\2\60\61\7k\2\2\61\62"+
		"\7p\2\2\62\63\7v\2\2\63\64\7t\2\2\64\65\7q\2\2\65\66\3\2\2\2\66\67\5\36"+
		"\17\2\678\3\2\2\289\b\2\2\29\5\3\2\2\2:;\7f\2\2;<\7g\2\2<=\7h\2\2=>\7"+
		"c\2\2>?\7w\2\2?@\7n\2\2@A\7v\2\2AB\3\2\2\2BC\5\36\17\2CD\3\2\2\2DE\b\3"+
		"\2\2E\7\3\2\2\2FG\7k\2\2GH\7p\2\2HI\7h\2\2IJ\7q\2\2JK\3\2\2\2KL\5\36\17"+
		"\2LM\3\2\2\2MN\b\4\2\2N\t\3\2\2\2OP\7q\2\2PQ\7r\2\2QR\7v\2\2RS\3\2\2\2"+
		"ST\7/\2\2TU\7x\2\2UV\7c\2\2VW\7n\2\2Wd\3\2\2\2Xe\5&\23\2YZ\5\36\17\2Z"+
		"_\5&\23\2[\\\7.\2\2\\^\5&\23\2][\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2"+
		"`b\3\2\2\2a_\3\2\2\2bc\5 \20\2ce\3\2\2\2dX\3\2\2\2dY\3\2\2\2ef\3\2\2\2"+
		"fg\b\5\2\2g\13\3\2\2\2hi\7u\2\2ij\7v\2\2jk\7c\2\2kl\7v\2\2lm\7w\2\2mn"+
		"\7u\2\2no\3\2\2\2op\5\36\17\2pq\3\2\2\2qr\b\6\2\2r\r\3\2\2\2st\7v\2\2"+
		"tu\7q\2\2uv\7e\2\2vw\3\2\2\2wx\5\36\17\2xy\5 \20\2y\17\3\2\2\2z{\7p\2"+
		"\2{|\7c\2\2|}\7o\2\2}~\7g\2\2~\177\7n\2\2\177\u0080\7k\2\2\u0080\u0081"+
		"\7u\2\2\u0081\u0082\7v\2\2\u0082\21\3\2\2\2\u0083\u0084\7x\2\2\u0084\u0085"+
		"\7c\2\2\u0085\u0086\7t\2\2\u0086\23\3\2\2\2\u0087\u0088\7x\2\2\u0088\u0089"+
		"\7c\2\2\u0089\u008a\7t\2\2\u008a\u008b\7i\2\2\u008b\u008c\7t\2\2\u008c"+
		"\u008d\7q\2\2\u008d\u008e\7w\2\2\u008e\u008f\7r\2\2\u008f\25\3\2\2\2\u0090"+
		"\u0091\7k\2\2\u0091\u0092\7p\2\2\u0092\u0093\7r\2\2\u0093\u0094\7w\2\2"+
		"\u0094\u0095\7v\2\2\u0095\u0096\7a\2\2\u0096\u0097\7f\2\2\u0097\u0098"+
		"\7k\2\2\u0098\u0099\7u\2\2\u0099\u009a\7e\2\2\u009a\u009b\7t\2\2\u009b"+
		"\u009c\7k\2\2\u009c\u009d\7r\2\2\u009d\u009e\7v\2\2\u009e\u009f\7k\2\2"+
		"\u009f\u00a0\7q\2\2\u00a0\u00a1\7p\2\2\u00a1\27\3\2\2\2\u00a2\u00a3\7"+
		"/\2\2\u00a3\u00a4\5\32\r\2\u00a4\31\3\2\2\2\u00a5\u00a6\t\2\2\2\u00a6"+
		"\33\3\2\2\2\u00a7\u00a8\t\3\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\b\16\3"+
		"\2\u00aa\35\3\2\2\2\u00ab\u00ac\7}\2\2\u00ac\37\3\2\2\2\u00ad\u00ae\7"+
		"\177\2\2\u00ae!\3\2\2\2\u00af\u00b0\7B\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2"+
		"\7g\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\5,\26\2\u00b5"+
		"#\3\2\2\2\u00b6\u00b7\7B\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\3\2\2\2\u00b9"+
		"\u00bf\5*\25\2\u00ba\u00bb\7B\2\2\u00bb\u00bc\7d\2\2\u00bc\u00bd\3\2\2"+
		"\2\u00bd\u00bf\5,\26\2\u00be\u00b6\3\2\2\2\u00be\u00ba\3\2\2\2\u00bf%"+
		"\3\2\2\2\u00c0\u00c4\7)\2\2\u00c1\u00c3\5,\26\2\u00c2\u00c1\3\2\2\2\u00c3"+
		"\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2"+
		"\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7)\2\2\u00c8\'\3\2\2\2\u00c9\u00ca"+
		"\7\60\2\2\u00ca\u00cb\7H\2\2\u00cb\u00cc\7C\2\2\u00cc\u00cd\7N\2\2\u00cd"+
		"\u00ce\7U\2\2\u00ce\u00cf\7G\2\2\u00cf\u00d7\7\60\2\2\u00d0\u00d1\7\60"+
		"\2\2\u00d1\u00d2\7V\2\2\u00d2\u00d3\7T\2\2\u00d3\u00d4\7W\2\2\u00d4\u00d5"+
		"\7G\2\2\u00d5\u00d7\7\60\2\2\u00d6\u00c9\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d7"+
		")\3\2\2\2\u00d8\u00dc\7}\2\2\u00d9\u00db\5,\26\2\u00da\u00d9\3\2\2\2\u00db"+
		"\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\3\2"+
		"\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\7\177\2\2\u00e0+\3\2\2\2\u00e1\u00e3"+
		"\n\4\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4"+
		"\u00e5\3\2\2\2\u00e5-\3\2\2\2\u00e6\u00e7\7\177\2\2\u00e7\u00e8\3\2\2"+
		"\2\u00e8\u00e9\b\27\4\2\u00e9/\3\2\2\2\13\2\3_d\u00be\u00c4\u00d6\u00dc"+
		"\u00e4\5\7\3\2\b\2\2\6\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}