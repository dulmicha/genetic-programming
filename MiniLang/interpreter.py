from antlr.MiniLangVisitor import MiniLangVisitor
from antlr.MiniLangParser import MiniLangParser
from antlr.MiniLangLexer import MiniLangLexer
from antlr.errors import *
from antlr4 import *


class Interpreter:
    @staticmethod
    def run(
        filename,
        inputs,
        from_file=True,
        instruction_limit=400,
        output_limit=1000,
        strict_mode=False,
    ):
        if from_file:
            input_stream = FileStream(filename, encoding="utf-8")
        else:
            input_stream = InputStream(filename)
        lexer = MiniLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiniLangParser(stream)
        tree = parser.program()
        visitor = MiniLangVisitor(inputs, instruction_limit, output_limit, strict_mode)
        try:
            visitor.visit(tree)
        except (
            InstructionLimitExceededException,
            OutputLimitExceededException,
            ZeroDivisionError,
        ) as e:
            print(e)

        return visitor.output, visitor.variables, visitor.instruction_counter


if __name__ == "__main__":
    file_path = "../antlr/test/test2.minilang"
    input_values = [7, 2, 3]
    result = Interpreter.run(file_path, input_values)
    print("Test result:", result)
