# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u0230\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\7\2\u008a\n\2\f\2\16\2\u008d\13\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0098\n\3\f\3\16\3\u009b")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\4\7\4\u00a2\n\4\f\4\16\4\u00a5")
        buf.write("\13\4\3\4\3\4\7\4\u00a9\n\4\f\4\16\4\u00ac\13\4\3\4\3")
        buf.write("\4\6\4\u00b0\n\4\r\4\16\4\u00b1\7\4\u00b4\n\4\f\4\16\4")
        buf.write("\u00b7\13\4\3\4\5\4\u00ba\n\4\3\5\3\5\6\5\u00be\n\5\r")
        buf.write("\5\16\5\u00bf\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u00c9\n")
        buf.write("\6\3\6\3\6\5\6\u00cd\n\6\3\6\3\6\3\7\3\7\3\7\7\7\u00d4")
        buf.write("\n\7\f\7\16\7\u00d7\13\7\3\7\3\7\7\7\u00db\n\7\f\7\16")
        buf.write("\7\u00de\13\7\3\7\5\7\u00e1\n\7\3\7\6\7\u00e4\n\7\r\7")
        buf.write("\16\7\u00e5\7\7\u00e8\n\7\f\7\16\7\u00eb\13\7\5\7\u00ed")
        buf.write("\n\7\3\b\3\b\7\b\u00f1\n\b\f\b\16\b\u00f4\13\b\3\b\6\b")
        buf.write("\u00f7\n\b\r\b\16\b\u00f8\3\b\5\b\u00fc\n\b\3\b\6\b\u00ff")
        buf.write("\n\b\r\b\16\b\u0100\7\b\u0103\n\b\f\b\16\b\u0106\13\b")
        buf.write("\3\b\5\b\u0109\n\b\3\t\3\t\5\t\u010d\n\t\3\t\6\t\u0110")
        buf.write("\n\t\r\t\16\t\u0111\3\t\6\t\u0115\n\t\r\t\16\t\u0116\3")
        buf.write("\t\5\t\u011a\n\t\3\t\6\t\u011d\n\t\r\t\16\t\u011e\7\t")
        buf.write("\u0121\n\t\f\t\16\t\u0124\13\t\5\t\u0126\n\t\3\n\3\n\5")
        buf.write("\n\u012a\n\n\3\13\3\13\7\13\u012e\n\13\f\13\16\13\u0131")
        buf.write("\13\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/")
        buf.write("\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\38\39\39\39\3:\3:\3:\3;\3;\7;\u01ee\n;\f;\16;\u01f1")
        buf.write("\13;\3<\6<\u01f4\n<\r<\16<\u01f5\3<\3<\3=\3=\7=\u01fc")
        buf.write("\n=\f=\16=\u01ff\13=\3=\5=\u0202\n=\3=\3=\3=\7=\u0207")
        buf.write("\n=\f=\16=\u020a\13=\3=\3=\3=\3=\7=\u0210\n=\f=\16=\u0213")
        buf.write("\13=\3=\5=\u0216\n=\3>\3>\7>\u021a\n>\f>\16>\u021d\13")
        buf.write(">\3>\3>\3>\3?\3?\5?\u0224\n?\3@\3@\3@\3A\3A\3A\5A\u022c")
        buf.write("\nA\3B\3B\3B\3\u008b\2C\3\3\5\4\7\5\t\6\13\7\r\2\17\2")
        buf.write("\21\2\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21")
        buf.write("\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34")
        buf.write("=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61")
        buf.write("g\62i\63k\64m\65o\66q\67s8u9w:y;{<}\2\177\2\u0081\2\u0083")
        buf.write("=\3\2\17\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2\62;aa\4\2G")
        buf.write("Ggg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"")
        buf.write("\"\b\3\n\f\16\17\"\"$$))^^\7\2\n\f\16\17$$))^^\n\2$$)")
        buf.write(")^^ddhhppttvv\3\2^^\2\u0254\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u0093\3\2\2\2\7\u00b9")
        buf.write("\3\2\2\2\t\u00bb\3\2\2\2\13\u00cc\3\2\2\2\r\u00ec\3\2")
        buf.write("\2\2\17\u00ee\3\2\2\2\21\u010a\3\2\2\2\23\u0129\3\2\2")
        buf.write("\2\25\u012b\3\2\2\2\27\u0135\3\2\2\2\31\u013a\3\2\2\2")
        buf.write("\33\u0140\3\2\2\2\35\u0148\3\2\2\2\37\u014b\3\2\2\2!\u0150")
        buf.write("\3\2\2\2#\u0156\3\2\2\2%\u015c\3\2\2\2\'\u0160\3\2\2\2")
        buf.write(")\u0169\3\2\2\2+\u016c\3\2\2\2-\u0174\3\2\2\2/\u017b\3")
        buf.write("\2\2\2\61\u0182\3\2\2\2\63\u0187\3\2\2\2\65\u018c\3\2")
        buf.write("\2\2\67\u0192\3\2\2\29\u0196\3\2\2\2;\u019f\3\2\2\2=\u01a2")
        buf.write("\3\2\2\2?\u01aa\3\2\2\2A\u01b0\3\2\2\2C\u01b2\3\2\2\2")
        buf.write("E\u01b4\3\2\2\2G\u01b6\3\2\2\2I\u01b8\3\2\2\2K\u01ba\3")
        buf.write("\2\2\2M\u01bc\3\2\2\2O\u01be\3\2\2\2Q\u01c0\3\2\2\2S\u01c2")
        buf.write("\3\2\2\2U\u01c4\3\2\2\2W\u01c6\3\2\2\2Y\u01c8\3\2\2\2")
        buf.write("[\u01ca\3\2\2\2]\u01cc\3\2\2\2_\u01ce\3\2\2\2a\u01d0\3")
        buf.write("\2\2\2c\u01d2\3\2\2\2e\u01d5\3\2\2\2g\u01d8\3\2\2\2i\u01db")
        buf.write("\3\2\2\2k\u01de\3\2\2\2m\u01e0\3\2\2\2o\u01e2\3\2\2\2")
        buf.write("q\u01e5\3\2\2\2s\u01e8\3\2\2\2u\u01eb\3\2\2\2w\u01f3\3")
        buf.write("\2\2\2y\u0215\3\2\2\2{\u0217\3\2\2\2}\u0223\3\2\2\2\177")
        buf.write("\u0225\3\2\2\2\u0081\u022b\3\2\2\2\u0083\u022d\3\2\2\2")
        buf.write("\u0085\u0086\7\61\2\2\u0086\u0087\7,\2\2\u0087\u008b\3")
        buf.write("\2\2\2\u0088\u008a\13\2\2\2\u0089\u0088\3\2\2\2\u008a")
        buf.write("\u008d\3\2\2\2\u008b\u008c\3\2\2\2\u008b\u0089\3\2\2\2")
        buf.write("\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\7")
        buf.write(",\2\2\u008f\u0090\7\61\2\2\u0090\u0091\3\2\2\2\u0091\u0092")
        buf.write("\b\2\2\2\u0092\4\3\2\2\2\u0093\u0094\7\61\2\2\u0094\u0095")
        buf.write("\7\61\2\2\u0095\u0099\3\2\2\2\u0096\u0098\n\2\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009c\u009d\b\3\2\2\u009d\6\3\2\2\2\u009e\u00ba")
        buf.write("\7\62\2\2\u009f\u00a3\t\3\2\2\u00a0\u00a2\t\4\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00ba\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00b5\t\3\2\2\u00a7\u00a9\t\4\2\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa")
        buf.write("\u00ab\3\2\2\2\u00ab\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ad\u00af\7a\2\2\u00ae\u00b0\t\4\2\2\u00af\u00ae\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00aa\3\2\2\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\b")
        buf.write("\4\3\2\u00b9\u009e\3\2\2\2\u00b9\u009f\3\2\2\2\u00b9\u00a6")
        buf.write("\3\2\2\2\u00ba\b\3\2\2\2\u00bb\u00bd\7\62\2\2\u00bc\u00be")
        buf.write("\t\5\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00c2\b\5\4\2\u00c2\n\3\2\2\2\u00c3\u00c4\5\r\7")
        buf.write("\2\u00c4\u00c5\5\17\b\2\u00c5\u00cd\3\2\2\2\u00c6\u00c8")
        buf.write("\5\r\7\2\u00c7\u00c9\5\17\b\2\u00c8\u00c7\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\5\21\t")
        buf.write("\2\u00cb\u00cd\3\2\2\2\u00cc\u00c3\3\2\2\2\u00cc\u00c6")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\b\6\5\2\u00cf")
        buf.write("\f\3\2\2\2\u00d0\u00ed\7\62\2\2\u00d1\u00d5\t\3\2\2\u00d2")
        buf.write("\u00d4\t\4\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00ed\3")
        buf.write("\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00e9\t\3\2\2\u00d9\u00db")
        buf.write("\t\4\2\2\u00da\u00d9\3\2\2\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e0\3\2\2\2")
        buf.write("\u00de\u00dc\3\2\2\2\u00df\u00e1\7a\2\2\u00e0\u00df\3")
        buf.write("\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e4")
        buf.write("\t\4\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2")
        buf.write("\u00e7\u00dc\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3")
        buf.write("\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00ec\u00d0\3\2\2\2\u00ec\u00d1\3\2\2\2\u00ec")
        buf.write("\u00d8\3\2\2\2\u00ed\16\3\2\2\2\u00ee\u0108\7\60\2\2\u00ef")
        buf.write("\u00f1\t\4\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2")
        buf.write("\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u0109\3")
        buf.write("\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f7\t\4\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u0104\3\2\2\2\u00fa\u00fc\7a\2\2")
        buf.write("\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3")
        buf.write("\2\2\2\u00fd\u00ff\t\4\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0103\3\2\2\2\u0102\u00fb\3\2\2\2\u0103\u0106\3\2\2\2")
        buf.write("\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0109\3")
        buf.write("\2\2\2\u0106\u0104\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u00f2")
        buf.write("\3\2\2\2\u0108\u00f6\3\2\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\20\3\2\2\2\u010a\u010c\t\6\2\2\u010b\u010d\t\7\2\2\u010c")
        buf.write("\u010b\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u0125\3\2\2\2")
        buf.write("\u010e\u0110\t\4\2\2\u010f\u010e\3\2\2\2\u0110\u0111\3")
        buf.write("\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0126")
        buf.write("\3\2\2\2\u0113\u0115\t\4\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u0122\3\2\2\2\u0118\u011a\7a\2\2\u0119\u0118\3")
        buf.write("\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u011d")
        buf.write("\t\4\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2")
        buf.write("\u0120\u0119\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0122\u0123\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122")
        buf.write("\3\2\2\2\u0125\u010f\3\2\2\2\u0125\u0114\3\2\2\2\u0126")
        buf.write("\22\3\2\2\2\u0127\u012a\5\61\31\2\u0128\u012a\5!\21\2")
        buf.write("\u0129\u0127\3\2\2\2\u0129\u0128\3\2\2\2\u012a\24\3\2")
        buf.write("\2\2\u012b\u012f\7$\2\2\u012c\u012e\5}?\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0132\u0133\7$\2\2\u0133\u0134\b\13\6\2\u0134\26\3\2")
        buf.write("\2\2\u0135\u0136\7c\2\2\u0136\u0137\7w\2\2\u0137\u0138")
        buf.write("\7v\2\2\u0138\u0139\7q\2\2\u0139\30\3\2\2\2\u013a\u013b")
        buf.write("\7d\2\2\u013b\u013c\7t\2\2\u013c\u013d\7g\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7m\2\2\u013f\32\3\2\2\2\u0140\u0141")
        buf.write("\7d\2\2\u0141\u0142\7q\2\2\u0142\u0143\7q\2\2\u0143\u0144")
        buf.write("\7n\2\2\u0144\u0145\7g\2\2\u0145\u0146\7c\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\34\3\2\2\2\u0148\u0149\7f\2\2\u0149\u014a")
        buf.write("\7q\2\2\u014a\36\3\2\2\2\u014b\u014c\7g\2\2\u014c\u014d")
        buf.write("\7n\2\2\u014d\u014e\7u\2\2\u014e\u014f\7g\2\2\u014f \3")
        buf.write("\2\2\2\u0150\u0151\7h\2\2\u0151\u0152\7c\2\2\u0152\u0153")
        buf.write("\7n\2\2\u0153\u0154\7u\2\2\u0154\u0155\7g\2\2\u0155\"")
        buf.write("\3\2\2\2\u0156\u0157\7h\2\2\u0157\u0158\7n\2\2\u0158\u0159")
        buf.write("\7q\2\2\u0159\u015a\7c\2\2\u015a\u015b\7v\2\2\u015b$\3")
        buf.write("\2\2\2\u015c\u015d\7h\2\2\u015d\u015e\7q\2\2\u015e\u015f")
        buf.write("\7t\2\2\u015f&\3\2\2\2\u0160\u0161\7h\2\2\u0161\u0162")
        buf.write("\7w\2\2\u0162\u0163\7p\2\2\u0163\u0164\7e\2\2\u0164\u0165")
        buf.write("\7v\2\2\u0165\u0166\7k\2\2\u0166\u0167\7q\2\2\u0167\u0168")
        buf.write("\7p\2\2\u0168(\3\2\2\2\u0169\u016a\7k\2\2\u016a\u016b")
        buf.write("\7h\2\2\u016b*\3\2\2\2\u016c\u016d\7k\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e\u016f\7v\2\2\u016f\u0170\7g\2\2\u0170\u0171")
        buf.write("\7i\2\2\u0171\u0172\7g\2\2\u0172\u0173\7t\2\2\u0173,\3")
        buf.write("\2\2\2\u0174\u0175\7t\2\2\u0175\u0176\7g\2\2\u0176\u0177")
        buf.write("\7v\2\2\u0177\u0178\7w\2\2\u0178\u0179\7t\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a.\3\2\2\2\u017b\u017c\7u\2\2\u017c\u017d")
        buf.write("\7v\2\2\u017d\u017e\7t\2\2\u017e\u017f\7k\2\2\u017f\u0180")
        buf.write("\7p\2\2\u0180\u0181\7i\2\2\u0181\60\3\2\2\2\u0182\u0183")
        buf.write("\7v\2\2\u0183\u0184\7t\2\2\u0184\u0185\7w\2\2\u0185\u0186")
        buf.write("\7g\2\2\u0186\62\3\2\2\2\u0187\u0188\7x\2\2\u0188\u0189")
        buf.write("\7q\2\2\u0189\u018a\7k\2\2\u018a\u018b\7f\2\2\u018b\64")
        buf.write("\3\2\2\2\u018c\u018d\7y\2\2\u018d\u018e\7j\2\2\u018e\u018f")
        buf.write("\7k\2\2\u018f\u0190\7n\2\2\u0190\u0191\7g\2\2\u0191\66")
        buf.write("\3\2\2\2\u0192\u0193\7q\2\2\u0193\u0194\7w\2\2\u0194\u0195")
        buf.write("\7v\2\2\u01958\3\2\2\2\u0196\u0197\7e\2\2\u0197\u0198")
        buf.write("\7q\2\2\u0198\u0199\7p\2\2\u0199\u019a\7v\2\2\u019a\u019b")
        buf.write("\7k\2\2\u019b\u019c\7p\2\2\u019c\u019d\7w\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019e:\3\2\2\2\u019f\u01a0\7q\2\2\u01a0\u01a1")
        buf.write("\7h\2\2\u01a1<\3\2\2\2\u01a2\u01a3\7k\2\2\u01a3\u01a4")
        buf.write("\7p\2\2\u01a4\u01a5\7j\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7")
        buf.write("\7t\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9\7v\2\2\u01a9>\3")
        buf.write("\2\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac\7t\2\2\u01ac\u01ad")
        buf.write("\7t\2\2\u01ad\u01ae\7c\2\2\u01ae\u01af\7{\2\2\u01af@\3")
        buf.write("\2\2\2\u01b0\u01b1\7?\2\2\u01b1B\3\2\2\2\u01b2\u01b3\7")
        buf.write("=\2\2\u01b3D\3\2\2\2\u01b4\u01b5\7.\2\2\u01b5F\3\2\2\2")
        buf.write("\u01b6\u01b7\7*\2\2\u01b7H\3\2\2\2\u01b8\u01b9\7+\2\2")
        buf.write("\u01b9J\3\2\2\2\u01ba\u01bb\7}\2\2\u01bbL\3\2\2\2\u01bc")
        buf.write("\u01bd\7\177\2\2\u01bdN\3\2\2\2\u01be\u01bf\7]\2\2\u01bf")
        buf.write("P\3\2\2\2\u01c0\u01c1\7_\2\2\u01c1R\3\2\2\2\u01c2\u01c3")
        buf.write("\7\60\2\2\u01c3T\3\2\2\2\u01c4\u01c5\7<\2\2\u01c5V\3\2")
        buf.write("\2\2\u01c6\u01c7\7-\2\2\u01c7X\3\2\2\2\u01c8\u01c9\7/")
        buf.write("\2\2\u01c9Z\3\2\2\2\u01ca\u01cb\7,\2\2\u01cb\\\3\2\2\2")
        buf.write("\u01cc\u01cd\7\61\2\2\u01cd^\3\2\2\2\u01ce\u01cf\7\'\2")
        buf.write("\2\u01cf`\3\2\2\2\u01d0\u01d1\7#\2\2\u01d1b\3\2\2\2\u01d2")
        buf.write("\u01d3\7(\2\2\u01d3\u01d4\7(\2\2\u01d4d\3\2\2\2\u01d5")
        buf.write("\u01d6\7~\2\2\u01d6\u01d7\7~\2\2\u01d7f\3\2\2\2\u01d8")
        buf.write("\u01d9\7?\2\2\u01d9\u01da\7?\2\2\u01dah\3\2\2\2\u01db")
        buf.write("\u01dc\7#\2\2\u01dc\u01dd\7?\2\2\u01ddj\3\2\2\2\u01de")
        buf.write("\u01df\7@\2\2\u01dfl\3\2\2\2\u01e0\u01e1\7>\2\2\u01e1")
        buf.write("n\3\2\2\2\u01e2\u01e3\7@\2\2\u01e3\u01e4\7?\2\2\u01e4")
        buf.write("p\3\2\2\2\u01e5\u01e6\7>\2\2\u01e6\u01e7\7?\2\2\u01e7")
        buf.write("r\3\2\2\2\u01e8\u01e9\7<\2\2\u01e9\u01ea\7<\2\2\u01ea")
        buf.write("t\3\2\2\2\u01eb\u01ef\t\b\2\2\u01ec\u01ee\t\t\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2")
        buf.write("\u01ef\u01f0\3\2\2\2\u01f0v\3\2\2\2\u01f1\u01ef\3\2\2")
        buf.write("\2\u01f2\u01f4\t\n\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u01f7\3\2\2\2\u01f7\u01f8\b<\2\2\u01f8x\3\2\2\2\u01f9")
        buf.write("\u01fd\7$\2\2\u01fa\u01fc\5}?\2\u01fb\u01fa\3\2\2\2\u01fc")
        buf.write("\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2")
        buf.write("\u01fe\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0202\t")
        buf.write("\13\2\2\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203")
        buf.write("\u0216\b=\7\2\u0204\u0208\7$\2\2\u0205\u0207\5}?\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207\u020a\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0208\u0209\3\2\2\2\u0209\u020b\3\2\2\2\u020a\u0208\3")
        buf.write("\2\2\2\u020b\u020c\7^\2\2\u020c\u020d\7$\2\2\u020d\u0211")
        buf.write("\3\2\2\2\u020e\u0210\5}?\2\u020f\u020e\3\2\2\2\u0210\u0213")
        buf.write("\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write("\u0214\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0216\b=\b\2")
        buf.write("\u0215\u01f9\3\2\2\2\u0215\u0204\3\2\2\2\u0216z\3\2\2")
        buf.write("\2\u0217\u021b\7$\2\2\u0218\u021a\5}?\2\u0219\u0218\3")
        buf.write("\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c")
        buf.write("\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b\3\2\2\2\u021e")
        buf.write("\u021f\5\u0081A\2\u021f\u0220\b>\t\2\u0220|\3\2\2\2\u0221")
        buf.write("\u0224\n\f\2\2\u0222\u0224\5\177@\2\u0223\u0221\3\2\2")
        buf.write("\2\u0223\u0222\3\2\2\2\u0224~\3\2\2\2\u0225\u0226\7^\2")
        buf.write("\2\u0226\u0227\t\r\2\2\u0227\u0080\3\2\2\2\u0228\u0229")
        buf.write("\7^\2\2\u0229\u022c\n\r\2\2\u022a\u022c\n\16\2\2\u022b")
        buf.write("\u0228\3\2\2\2\u022b\u022a\3\2\2\2\u022c\u0082\3\2\2\2")
        buf.write("\u022d\u022e\13\2\2\2\u022e\u022f\bB\n\2\u022f\u0084\3")
        buf.write("\2\2\2,\2\u008b\u0099\u00a3\u00aa\u00b1\u00b5\u00b9\u00bf")
        buf.write("\u00c8\u00cc\u00d5\u00dc\u00e0\u00e5\u00e9\u00ec\u00f2")
        buf.write("\u00f8\u00fb\u0100\u0104\u0108\u010c\u0111\u0116\u0119")
        buf.write("\u011e\u0122\u0125\u0129\u012f\u01ef\u01f5\u01fd\u0201")
        buf.write("\u0208\u0211\u0215\u021b\u0223\u022b\13\b\2\2\3\4\2\3")
        buf.write("\5\3\3\6\4\3\13\5\3=\6\3=\7\3>\b\3B\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    LINE_COMMENT = 2
    INTLIT = 3
    INLIT_ERROR_0 = 4
    FLOATLIT = 5
    BOOLLIT = 6
    STRINGLIT = 7
    AUTO = 8
    BREAK = 9
    BOOLEAN = 10
    DO = 11
    ELSE = 12
    FALSE = 13
    FLOAT = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    INTEGER = 18
    RETURN = 19
    STRING = 20
    TRUE = 21
    VOID = 22
    WHILE = 23
    OUT = 24
    CONTINUE = 25
    OF = 26
    INHERIT = 27
    ARRAY = 28
    EQUAL = 29
    SEMI = 30
    COMMA = 31
    LB = 32
    RB = 33
    LCB = 34
    RCB = 35
    LSB = 36
    RSB = 37
    DOT = 38
    DDOT = 39
    ADD = 40
    SUB = 41
    MUL = 42
    DIV = 43
    MOD = 44
    NOT = 45
    AND = 46
    OR = 47
    EQUALTO = 48
    NOTEQ = 49
    GREAT = 50
    LESS = 51
    GREATEQ = 52
    LESSEQ = 53
    SCOPE = 54
    IDENTIFIER = 55
    WS = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'void'", "'while'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'='", "';'", "','", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "'.'", "':'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'>'", "'<'", "'>='", "'<='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "INTLIT", "INLIT_ERROR_0", 
            "FLOATLIT", "BOOLLIT", "STRINGLIT", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "EQUAL", "SEMI", "COMMA", "LB", "RB", 
            "LCB", "RCB", "LSB", "RSB", "DOT", "DDOT", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQUALTO", "NOTEQ", "GREAT", 
            "LESS", "GREATEQ", "LESSEQ", "SCOPE", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BLOCK_COMMENT", "LINE_COMMENT", "INTLIT", "INLIT_ERROR_0", 
                  "FLOATLIT", "INT_PART", "DEC_PART", "EXP_PART", "BOOLLIT", 
                  "STRINGLIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "EQUAL", "SEMI", "COMMA", "LB", 
                  "RB", "LCB", "RCB", "LSB", "RSB", "DOT", "DDOT", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUALTO", 
                  "NOTEQ", "GREAT", "LESS", "GREATEQ", "LESSEQ", "SCOPE", 
                  "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.INTLIT_action 
            actions[3] = self.INLIT_ERROR_0_action 
            actions[4] = self.FLOATLIT_action 
            actions[9] = self.STRINGLIT_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def INLIT_ERROR_0_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken("0")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\', '\\"']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

        if actionIndex == 5:
             raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            		raise ErrorToken(self.text)
            	
     


