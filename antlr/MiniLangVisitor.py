# Generated from C:/Users/wehil/PycharmProjects/genetic-programming/antlr/MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser


# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    def __init__(self, input_values=None, instruction_limit=100, output_limit=10):
        if input_values is None:
            input_values = []
        self.variables = {}
        self.output = []
        self.output_limit = output_limit
        self.input_values = input_values
        self.input_index = 0
        self.instruction_limit = instruction_limit
        self.instruction_counter = 0

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx: MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLangParser#instruction.
    def visitInstruction(self, ctx: MiniLangParser.InstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLangParser#if.
    def visitIf(self, ctx: MiniLangParser.IfContext):
        self.instruction_counter += 1
        if self.instruction_counter >= self.instruction_limit:
            raise Exception("Przekroczono limit instrukcji")
        condition = self.visitCondition(ctx.getChild(2))
        if condition:
            self.visitBlock_statement(ctx.getChild(4))

    # Visit a parse tree produced by MiniLangParser#condition.
    def visitCondition(self, ctx: MiniLangParser.ConditionContext):
        final_condition = self.visitCondition_body(ctx.getChild(0))
        if ctx.getChildCount() > 1:
            for i in range(1, ctx.getChildCount(), 2):
                next_condition = self.visitCondition_body(ctx.getChild(i + 1))
                logical_operator = ctx.getChild(i).getText()
                if logical_operator == 'and':
                    final_condition = final_condition and next_condition
                else:
                    final_condition = final_condition or next_condition
        return final_condition

    # Visit a parse tree produced by MiniLangParser#condition_body.
    def visitCondition_body(self, ctx: MiniLangParser.Condition_bodyContext):
        left_value = self.visitExpression(ctx.getChild(0))
        if ctx.getChild(2).getText() == 'True' or ctx.getChild(2).getText() == 'False':
            right_value = self.visitBoolean(ctx.getChild(2))
        else:
            right_value = self.visitExpression(ctx.getChild(2))
        operator = ctx.getChild(1).getText()
        operation = {'>': lambda x, y: x > y,
                     '<': lambda x, y: x < y,
                     '==': lambda x, y: x == y,
                     '!=': lambda x, y: x != y,
                     '<=': lambda x, y: x <= y,
                     '>=': lambda x, y: x >= y}
        return operation[operator](left_value, right_value)

    # Visit a parse tree produced by MiniLangParser#input.
    def visitInput(self, ctx: MiniLangParser.InputContext):  # TODO
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: MiniLangParser.AssignmentContext):
        self.instruction_counter += 1
        if self.instruction_counter >= self.instruction_limit:
            raise Exception("Przekroczono limit instrukcji")
        variable_name = ctx.getChild(0).getText()
        if not self.variables.get(str(variable_name)):
            self.variables[variable_name] = 0
        variable_value = self.visitExpression(ctx.getChild(2))
        self.variables[variable_name] = variable_value

    # Visit a parse tree produced by MiniLangParser#expression.
    def visitExpression(self, ctx: MiniLangParser.ExpressionContext):
        if ctx.integer():
            return self.visitInteger(ctx.getChild(0))
        elif ctx.var():
            variable_name = ctx.getChild(0).getText()
            if variable_name in self.variables:
                variable_name = ctx.getText()
                return self.variables.get(variable_name)
            else:
                raise Exception("Zmienna niezainicjalizowana")
        elif ctx.math_expression():
            return self.visitMath_expression(ctx.getChild(0))

    # Visit a parse tree produced by MiniLangParser#math_expression.
    def visitMath_expression(self, ctx: MiniLangParser.Math_expressionContext):
        left_value = self.visit(ctx.getChild(1))
        right_value = self.visit(ctx.getChild(3))
        operator = ctx.getChild(2).getText()
        operation = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y}
        if operator == '/':
            if right_value == 0:
                raise Exception("Dzielenie przez zero")
            else:
                return left_value / right_value
        return operation[operator](left_value, right_value)

    # Visit a parse tree produced by MiniLangParser#block_statement.
    def visitBlock_statement(self, ctx: MiniLangParser.Block_statementContext):
        for instruction in ctx.getChildren():
            if self.instruction_counter >= self.instruction_limit:
                raise Exception("Przekroczono limit instrukcji")
            self.visit(instruction)

    # Visit a parse tree produced by MiniLangParser#loop.
    def visitLoop(self, ctx: MiniLangParser.LoopContext):
        iterations = int(ctx.getChild(1).getText())
        for _ in range(iterations):
            self.instruction_counter += 1
            if self.instruction_counter >= self.instruction_limit:
                raise Exception("Przekroczono limit instrukcji")
            self.visitBlock_statement(ctx.getChild(2))

    # Visit a parse tree produced by MiniLangParser#print.
    def visitPrint(self, ctx: MiniLangParser.PrintContext):
        self.instruction_counter += 1
        if self.instruction_counter >= self.instruction_limit:
            raise Exception("Przekroczono limit instrukcji")
        if len(self.output) >= self.output_limit:
            raise Exception("Przekroczono limit wyjścia")
        self.output.append(self.visitExpression(ctx.getChild(2)))

    # Visit a parse tree produced by MiniLangParser#var.
    def visitVar(self, ctx: MiniLangParser.VarContext):
        return ctx.getText()

    # Visit a parse tree produced by MiniLangParser#nonzero_digit.
    def visitNonzero_digit(self, ctx: MiniLangParser.Nonzero_digitContext):
        return int(ctx.getText())

    # Visit a parse tree produced by MiniLangParser#integer.
    def visitInteger(self, ctx: MiniLangParser.IntegerContext):
        return int(ctx.getText())

    # Visit a parse tree produced by MiniLangParser#boolean.
    def visitBoolean(self, ctx: MiniLangParser.BooleanContext):
        return ctx.getText() == 'True'


del MiniLangParser
