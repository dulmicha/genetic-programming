from antlr.MiniLangVisitor import MiniLangVisitor
from antlr.MiniLangParser import MiniLangParser
from antlr.MiniLangLexer import MiniLangLexer
from antlr4 import *


def interpreter(filename, inputs):
    input_stream = FileStream(filename, encoding='utf-8')
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.program()
    visitor = MiniLangVisitor(inputs)
    visitor.visit(tree)
    return visitor.output, visitor.variables, visitor.instruction_counter


file_path = '../antlr/test/test2.minilang'
input_values = [7, 2, 3]
result = interpreter(file_path, input_values)
print("Wynik testu:", result)
