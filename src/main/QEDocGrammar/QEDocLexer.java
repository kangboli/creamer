// Generated from QEDocLexer.g4 by ANTLR 4.9
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
		TextBegin=6, TitleBegin=7, DistributionBegin=8, TOC=9, NameList=10, Var=11, 
		VarGroup=12, InputDiscription=13, Options=14, Section=15, Subsection=16, 
		Flag=17, String=18, ID=19, WS=20, OB=21, CB=22, Ref=23, BoldText=24, TTText=25, 
		StringText=26, LogicalText=27, ScopedText=28, WordText=29, WST=30, EndText=31;
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
			"TextBegin", "TitleBegin", "DistributionBegin", "TOC", "NameList", "Var", 
			"VarGroup", "InputDiscription", "Options", "Section", "Subsection", "Flag", 
			"String", "ID", "Word", "WS", "OB", "CB", "Ref", "BoldText", "TTText", 
			"StringText", "LogicalText", "ScopedText", "WordText", "WST", "EndText"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "'namelist'", 
			"'var'", "'vargroup'", "'input_description'", "'options'", "'section'", 
			"'subsection'", null, null, null, null, "'{'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IntroBegin", "DefaultBegin", "InfoBegin", "OptBegin", "StatusBegin", 
			"TextBegin", "TitleBegin", "DistributionBegin", "TOC", "NameList", "Var", 
			"VarGroup", "InputDiscription", "Options", "Section", "Subsection", "Flag", 
			"String", "ID", "WS", "OB", "CB", "Ref", "BoldText", "TTText", "StringText", 
			"LogicalText", "ScopedText", "WordText", "WST", "EndText"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2!\u01b5\b\1\b\1\4"+
		"\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n"+
		"\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2L\n\2\3\2\3\2\3\2\3\2\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3[\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\5\4g\n\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\6\5r\n\5\r\5\16\5"+
		"s\3\5\3\5\3\5\3\5\3\5\3\5\5\5|\n\5\3\5\3\5\3\5\5\5\u0081\n\5\3\5\3\5\5"+
		"\5\u0085\n\5\3\5\3\5\5\5\u0089\n\5\3\5\3\5\5\5\u008d\n\5\7\5\u008f\n\5"+
		"\f\5\16\5\u0092\13\5\5\5\u0094\n\5\3\5\5\5\u0097\n\5\3\5\3\5\3\5\3\5\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00a5\n\6\3\6\3\6\3\6\3\6\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\5\7\u00b1\n\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\5\b\u00bf\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\6\t\u00d4\n\t\r\t\16\t\u00d5\3\t\3\t\3\t\3"+
		"\t\3\n\3\n\3\n\3\n\3\n\5\n\u00e1\n\n\3\n\3\n\5\n\u00e5\n\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\5\23\u0131"+
		"\n\23\3\23\7\23\u0134\n\23\f\23\16\23\u0137\13\23\3\23\5\23\u013a\n\23"+
		"\3\23\3\23\3\24\3\24\3\25\6\25\u0141\n\25\r\25\16\25\u0142\3\26\6\26\u0146"+
		"\n\26\r\26\16\26\u0147\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3"+
		"\31\3\31\3\31\5\31\u0156\n\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u015e"+
		"\n\32\3\32\3\32\3\32\3\32\5\32\u0164\n\32\3\33\3\33\3\33\3\33\3\33\5\33"+
		"\u016b\n\33\3\33\3\33\3\33\3\33\5\33\u0171\n\33\3\34\3\34\5\34\u0175\n"+
		"\34\3\34\5\34\u0178\n\34\3\34\3\34\5\34\u017c\n\34\7\34\u017e\n\34\f\34"+
		"\16\34\u0181\13\34\3\34\5\34\u0184\n\34\3\34\3\34\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0195\n\35\3\36\3\36"+
		"\5\36\u0199\n\36\3\36\3\36\5\36\u019d\n\36\7\36\u019f\n\36\f\36\16\36"+
		"\u01a2\13\36\3\36\3\36\3\37\6\37\u01a7\n\37\r\37\16\37\u01a8\3 \6 \u01ac"+
		"\n \r \16 \u01ad\3 \3 \3!\3!\3!\3!\2\2\"\4\3\6\4\b\5\n\6\f\7\16\b\20\t"+
		"\22\n\24\13\26\f\30\r\32\16\34\17\36\20 \21\"\22$\23&\24(\25*\2,\26.\27"+
		"\60\30\62\31\64\32\66\338\34:\35<\36>\37@ B!\4\2\3\5\7\2\60\60\63;C\\"+
		"aac|\5\2\13\f\17\17\"\"\b\2\13\f\17\17\"\"BB}}\177\177\2\u01dd\2\4\3\2"+
		"\2\2\2\6\3\2\2\2\2\b\3\2\2\2\2\n\3\2\2\2\2\f\3\2\2\2\2\16\3\2\2\2\2\20"+
		"\3\2\2\2\2\22\3\2\2\2\2\24\3\2\2\2\2\26\3\2\2\2\2\30\3\2\2\2\2\32\3\2"+
		"\2\2\2\34\3\2\2\2\2\36\3\2\2\2\2 \3\2\2\2\2\"\3\2\2\2\2$\3\2\2\2\2&\3"+
		"\2\2\2\2(\3\2\2\2\2,\3\2\2\2\2.\3\2\2\2\2\60\3\2\2\2\3\62\3\2\2\2\3\64"+
		"\3\2\2\2\3\66\3\2\2\2\38\3\2\2\2\3:\3\2\2\2\3<\3\2\2\2\3>\3\2\2\2\3@\3"+
		"\2\2\2\3B\3\2\2\2\4D\3\2\2\2\6Q\3\2\2\2\b`\3\2\2\2\nl\3\2\2\2\f\u009c"+
		"\3\2\2\2\16\u00aa\3\2\2\2\20\u00b6\3\2\2\2\22\u00c4\3\2\2\2\24\u00db\3"+
		"\2\2\2\26\u00e8\3\2\2\2\30\u00f1\3\2\2\2\32\u00f5\3\2\2\2\34\u00fe\3\2"+
		"\2\2\36\u0110\3\2\2\2 \u0118\3\2\2\2\"\u0120\3\2\2\2$\u012b\3\2\2\2&\u012e"+
		"\3\2\2\2(\u013d\3\2\2\2*\u0140\3\2\2\2,\u0145\3\2\2\2.\u014b\3\2\2\2\60"+
		"\u014d\3\2\2\2\62\u014f\3\2\2\2\64\u0159\3\2\2\2\66\u0165\3\2\2\28\u0172"+
		"\3\2\2\2:\u0194\3\2\2\2<\u0196\3\2\2\2>\u01a6\3\2\2\2@\u01ab\3\2\2\2B"+
		"\u01b1\3\2\2\2DE\7k\2\2EF\7p\2\2FG\7v\2\2GH\7t\2\2HI\7q\2\2IK\3\2\2\2"+
		"JL\5,\26\2KJ\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\5.\27\2NO\3\2\2\2OP\b\2\2\2"+
		"P\5\3\2\2\2QR\7f\2\2RS\7g\2\2ST\7h\2\2TU\7c\2\2UV\7w\2\2VW\7n\2\2WX\7"+
		"v\2\2XZ\3\2\2\2Y[\5,\26\2ZY\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\5.\27\2]^"+
		"\3\2\2\2^_\b\3\2\2_\7\3\2\2\2`a\7k\2\2ab\7p\2\2bc\7h\2\2cd\7q\2\2df\3"+
		"\2\2\2eg\5,\26\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\5.\27\2ij\3\2\2\2jk\b"+
		"\4\2\2k\t\3\2\2\2lm\7q\2\2mn\7r\2\2no\7v\2\2oq\3\2\2\2pr\5,\26\2qp\3\2"+
		"\2\2rs\3\2\2\2sq\3\2\2\2st\3\2\2\2tu\3\2\2\2uv\7/\2\2vw\7x\2\2wx\7c\2"+
		"\2xy\7n\2\2y{\3\2\2\2z|\5,\26\2{z\3\2\2\2{|\3\2\2\2|\u0093\3\2\2\2}\u0094"+
		"\5&\23\2~\u0080\5.\27\2\177\u0081\5,\26\2\u0080\177\3\2\2\2\u0080\u0081"+
		"\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\5&\23\2\u0083\u0085\5,\26\2\u0084"+
		"\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0090\3\2\2\2\u0086\u0088\7."+
		"\2\2\u0087\u0089\5,\26\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089"+
		"\u008a\3\2\2\2\u008a\u008c\5&\23\2\u008b\u008d\5,\26\2\u008c\u008b\3\2"+
		"\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u0086\3\2\2\2\u008f"+
		"\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0094\3\2"+
		"\2\2\u0092\u0090\3\2\2\2\u0093}\3\2\2\2\u0093~\3\2\2\2\u0094\u0096\3\2"+
		"\2\2\u0095\u0097\5,\26\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097"+
		"\u0098\3\2\2\2\u0098\u0099\5.\27\2\u0099\u009a\3\2\2\2\u009a\u009b\b\5"+
		"\2\2\u009b\13\3\2\2\2\u009c\u009d\7u\2\2\u009d\u009e\7v\2\2\u009e\u009f"+
		"\7c\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7u\2\2\u00a2"+
		"\u00a4\3\2\2\2\u00a3\u00a5\5,\26\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2"+
		"\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\5.\27\2\u00a7\u00a8\3\2\2\2\u00a8"+
		"\u00a9\b\6\2\2\u00a9\r\3\2\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7g\2\2\u00ac"+
		"\u00ad\7z\2\2\u00ad\u00ae\7v\2\2\u00ae\u00b0\3\2\2\2\u00af\u00b1\5,\26"+
		"\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3"+
		"\5.\27\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\b\7\2\2\u00b5\17\3\2\2\2\u00b6"+
		"\u00b7\7/\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7v\2\2"+
		"\u00ba\u00bb\7n\2\2\u00bb\u00bc\7g\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bf"+
		"\5,\26\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0"+
		"\u00c1\5.\27\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b\b\2\2\u00c3\21\3\2\2"+
		"\2\u00c4\u00c5\7/\2\2\u00c5\u00c6\7f\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8"+
		"\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb"+
		"\u00cc\7d\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7k\2\2"+
		"\u00cf\u00d0\7q\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d4"+
		"\5,\26\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5"+
		"\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\5.\27\2\u00d8\u00d9\3\2"+
		"\2\2\u00d9\u00da\b\t\2\2\u00da\23\3\2\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd"+
		"\7q\2\2\u00dd\u00de\7e\2\2\u00de\u00e0\3\2\2\2\u00df\u00e1\5,\26\2\u00e0"+
		"\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e4\5."+
		"\27\2\u00e3\u00e5\5,\26\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5"+
		"\u00e6\3\2\2\2\u00e6\u00e7\5\60\30\2\u00e7\25\3\2\2\2\u00e8\u00e9\7p\2"+
		"\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7o\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed"+
		"\7n\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7v\2\2\u00f0"+
		"\27\3\2\2\2\u00f1\u00f2\7x\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7t\2\2\u00f4"+
		"\31\3\2\2\2\u00f5\u00f6\7x\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7t\2\2\u00f8"+
		"\u00f9\7i\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7w\2\2"+
		"\u00fc\u00fd\7r\2\2\u00fd\33\3\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7"+
		"p\2\2\u0100\u0101\7r\2\2\u0101\u0102\7w\2\2\u0102\u0103\7v\2\2\u0103\u0104"+
		"\7a\2\2\u0104\u0105\7f\2\2\u0105\u0106\7g\2\2\u0106\u0107\7u\2\2\u0107"+
		"\u0108\7e\2\2\u0108\u0109\7t\2\2\u0109\u010a\7k\2\2\u010a\u010b\7r\2\2"+
		"\u010b\u010c\7v\2\2\u010c\u010d\7k\2\2\u010d\u010e\7q\2\2\u010e\u010f"+
		"\7p\2\2\u010f\35\3\2\2\2\u0110\u0111\7q\2\2\u0111\u0112\7r\2\2\u0112\u0113"+
		"\7v\2\2\u0113\u0114\7k\2\2\u0114\u0115\7q\2\2\u0115\u0116\7p\2\2\u0116"+
		"\u0117\7u\2\2\u0117\37\3\2\2\2\u0118\u0119\7u\2\2\u0119\u011a\7g\2\2\u011a"+
		"\u011b\7e\2\2\u011b\u011c\7v\2\2\u011c\u011d\7k\2\2\u011d\u011e\7q\2\2"+
		"\u011e\u011f\7p\2\2\u011f!\3\2\2\2\u0120\u0121\7u\2\2\u0121\u0122\7w\2"+
		"\2\u0122\u0123\7d\2\2\u0123\u0124\7u\2\2\u0124\u0125\7g\2\2\u0125\u0126"+
		"\7e\2\2\u0126\u0127\7v\2\2\u0127\u0128\7k\2\2\u0128\u0129\7q\2\2\u0129"+
		"\u012a\7p\2\2\u012a#\3\2\2\2\u012b\u012c\7/\2\2\u012c\u012d\5(\24\2\u012d"+
		"%\3\2\2\2\u012e\u0130\7)\2\2\u012f\u0131\5,\26\2\u0130\u012f\3\2\2\2\u0130"+
		"\u0131\3\2\2\2\u0131\u0135\3\2\2\2\u0132\u0134\5*\25\2\u0133\u0132\3\2"+
		"\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136"+
		"\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u013a\5,\26\2\u0139\u0138\3\2"+
		"\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\7)\2\2\u013c"+
		"\'\3\2\2\2\u013d\u013e\5*\25\2\u013e)\3\2\2\2\u013f\u0141\t\2\2\2\u0140"+
		"\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2"+
		"\2\2\u0143+\3\2\2\2\u0144\u0146\t\3\2\2\u0145\u0144\3\2\2\2\u0146\u0147"+
		"\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2\u0149"+
		"\u014a\b\26\3\2\u014a-\3\2\2\2\u014b\u014c\7}\2\2\u014c/\3\2\2\2\u014d"+
		"\u014e\7\177\2\2\u014e\61\3\2\2\2\u014f\u0150\7B\2\2\u0150\u0151\7t\2"+
		"\2\u0151\u0152\7g\2\2\u0152\u0153\7h\2\2\u0153\u0155\3\2\2\2\u0154\u0156"+
		"\5@ \2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157"+
		"\u0158\5>\37\2\u0158\63\3\2\2\2\u0159\u015a\7B\2\2\u015a\u015b\7d\2\2"+
		"\u015b\u015d\3\2\2\2\u015c\u015e\5@ \2\u015d\u015c\3\2\2\2\u015d\u015e"+
		"\3\2\2\2\u015e\u0163\3\2\2\2\u015f\u0164\58\34\2\u0160\u0164\5:\35\2\u0161"+
		"\u0164\5<\36\2\u0162\u0164\5>\37\2\u0163\u015f\3\2\2\2\u0163\u0160\3\2"+
		"\2\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164\65\3\2\2\2\u0165\u0166"+
		"\7B\2\2\u0166\u0167\7v\2\2\u0167\u0168\7v\2\2\u0168\u016a\3\2\2\2\u0169"+
		"\u016b\5@ \2\u016a\u0169\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u0170\3\2\2"+
		"\2\u016c\u0171\58\34\2\u016d\u0171\5:\35\2\u016e\u0171\5<\36\2\u016f\u0171"+
		"\5>\37\2\u0170\u016c\3\2\2\2\u0170\u016d\3\2\2\2\u0170\u016e\3\2\2\2\u0170"+
		"\u016f\3\2\2\2\u0171\67\3\2\2\2\u0172\u0174\7)\2\2\u0173\u0175\5@ \2\u0174"+
		"\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u017f\3\2\2\2\u0176\u0178\5@"+
		" \2\u0177\u0176\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179"+
		"\u017b\5>\37\2\u017a\u017c\5@ \2\u017b\u017a\3\2\2\2\u017b\u017c\3\2\2"+
		"\2\u017c\u017e\3\2\2\2\u017d\u0177\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d"+
		"\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0182"+
		"\u0184\5@ \2\u0183\u0182\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\3\2\2"+
		"\2\u0185\u0186\7)\2\2\u01869\3\2\2\2\u0187\u0188\7\60\2\2\u0188\u0189"+
		"\7H\2\2\u0189\u018a\7C\2\2\u018a\u018b\7N\2\2\u018b\u018c\7U\2\2\u018c"+
		"\u018d\7G\2\2\u018d\u0195\7\60\2\2\u018e\u018f\7\60\2\2\u018f\u0190\7"+
		"V\2\2\u0190\u0191\7T\2\2\u0191\u0192\7W\2\2\u0192\u0193\7G\2\2\u0193\u0195"+
		"\7\60\2\2\u0194\u0187\3\2\2\2\u0194\u018e\3\2\2\2\u0195;\3\2\2\2\u0196"+
		"\u01a0\7}\2\2\u0197\u0199\5@ \2\u0198\u0197\3\2\2\2\u0198\u0199\3\2\2"+
		"\2\u0199\u019a\3\2\2\2\u019a\u019c\5>\37\2\u019b\u019d\5@ \2\u019c\u019b"+
		"\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u0198\3\2\2\2\u019f"+
		"\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\3\2"+
		"\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a4\7\177\2\2\u01a4=\3\2\2\2\u01a5\u01a7"+
		"\n\4\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8"+
		"\u01a9\3\2\2\2\u01a9?\3\2\2\2\u01aa\u01ac\t\3\2\2\u01ab\u01aa\3\2\2\2"+
		"\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af"+
		"\3\2\2\2\u01af\u01b0\b \3\2\u01b0A\3\2\2\2\u01b1\u01b2\7\177\2\2\u01b2"+
		"\u01b3\3\2\2\2\u01b3\u01b4\b!\4\2\u01b4C\3\2\2\2+\2\3KZfs{\u0080\u0084"+
		"\u0088\u008c\u0090\u0093\u0096\u00a4\u00b0\u00be\u00d5\u00e0\u00e4\u0130"+
		"\u0135\u0139\u0142\u0147\u0155\u015d\u0163\u016a\u0170\u0174\u0177\u017b"+
		"\u017f\u0183\u0194\u0198\u019c\u01a0\u01a8\u01ad\5\7\3\2\b\2\2\6\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}