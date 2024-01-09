from antlr.MiniLangVisitor import MiniLangVisitor
from antlr.MiniLangParser import MiniLangParser
from antlr.MiniLangLexer import MiniLangLexer
from antlr4 import *


def interpreter():
    lexer = MiniLangLexer(InputStream("X_1 = 0;for 5 {X_1 = (X_1 + 1);if (X_1 > 3 and X_1 < 5) {print(X_1);}}"))
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.program()
    visitor = MiniLangVisitor()
    visitor.visit(tree)
    return visitor.output, visitor.variables, visitor.instruction_counter


result = interpreter()
print("Wynik testu:", result)
