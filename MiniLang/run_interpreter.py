from antlr.MiniLangVisitor import MiniLangVisitor
from antlr.MiniLangParser import MiniLangParser
from antlr.MiniLangLexer import MiniLangLexer
from antlr4 import *


def interpreter():
    lexer = MiniLangLexer(InputStream("X_0 = 3; X_1 = input();"))
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.program()
    visitor = MiniLangVisitor()
    visitor.visit(tree)
    return visitor.output, visitor.variables, visitor.instruction_counter


result = interpreter()
print("Wynik testu:", result)
