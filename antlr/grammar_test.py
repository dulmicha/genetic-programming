import os
from antlr4 import *

from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser


def grammar_test(filepath):
    try:
        input_stream = FileStream(filepath)
        lexer = MiniLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiniLangParser(stream)

        tree = parser.program()
        print(f"Tested: {filepath}\nParse Tree: {tree.toStringTree(recog=parser)}\n")
    except Exception as e:
        print(f"Error testing {filepath}: {e}")


def get_test_files(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.minilang')]


if __name__ == '__main__':
    test_directory = "test"
    test_files = get_test_files(test_directory)

    for file_path in test_files:
        grammar_test(file_path)
