# Generated from C:/Users/wehil/PycharmProjects/genetic-programming/antlr/MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
from antlr.errors import *
import random

if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser


# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    def __init__(self, input_values=None, instruction_limit=10, output_limit=1000, strict_mode=False):
        self.variables = {}
        self.output = []
        self.output_limit = output_limit
        self.input_values = input_values
        self.input_index = 0
        self.instruction_limit = instruction_limit
        self.instruction_counter = 0
        self.strict_mode = strict_mode

    def get_next_input(self):
        if self.input_index >= len(self.input_values):
            self.input_index = 0
        value = self.input_values[self.input_index]
        self.input_index += 1
        if isinstance(value, str):
            if value not in self.variables:
                self.variables[value] = random.randint(1, 100)
            return self.variables[value]
        elif isinstance(value, int):
            return value

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx: MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLangParser#instruction.
    def visitInstruction(self, ctx: MiniLangParser.InstructionContext):
        self.instruction_counter += 1
        if self.instruction_counter >= self.instruction_limit:
            raise InstructionLimitExceededException("Przekroczono limit instrukcji")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLangParser#if.
    def visitIf(self, ctx: MiniLangParser.IfContext):
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
    def visitInput(self, ctx: MiniLangParser.InputContext):
        if self.input_index >= len(self.input_values):
            self.input_index = 0
        value = self.input_values[self.input_index]
        self.input_index += 1
        if isinstance(value, str):
            if value not in self.variables:
                self.variables[value] = random.randint(1, 100)
            return self.variables[value]
        elif isinstance(value, int):
            return value

    def visitAssignment(self, ctx: MiniLangParser.AssignmentContext):
        variable_name = ctx.getChild(0).getText()
        if ctx.expression():
            variable_value = self.visitExpression(ctx.getChild(2))
        else:
            variable_value = self.visitInput(ctx.getChild(2))
        self.variables[variable_name] = variable_value

    # Visit a parse tree produced by MiniLangParser#expression.
    def visitExpression(self, ctx: MiniLangParser.ExpressionContext):
        if ctx.integer():
            return self.visitInteger(ctx.getChild(0))
        elif ctx.var() and self.strict_mode:
            variable_name = ctx.getChild(0).getText()
            if variable_name in self.variables:
                variable_name = ctx.getText()
                return self.variables.get(variable_name)
            else:
                raise VariableNotInitializedException("Zmienna niezainicjalizowana")
        elif ctx.var():
            variable_name = ctx.getChild(0).getText()
            if variable_name not in self.variables:
                self.variables[variable_name] = self.get_next_input()
            return self.variables[variable_name]
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
                raise ZeroDivisionError("Dzielenie przez 0")
            else:
                return left_value // right_value
        return operation[operator](left_value, right_value)

    # Visit a parse tree produced by MiniLangParser#block_statement.
    def visitBlock_statement(self, ctx: MiniLangParser.Block_statementContext):
        for instruction in ctx.getChildren():
            if self.instruction_counter >= self.instruction_limit:
                raise InstructionLimitExceededException("Przekroczono limit instrukcji")
            self.visit(instruction)

    # Visit a parse tree produced by MiniLangParser#loop.
    def visitLoop(self, ctx: MiniLangParser.LoopContext):
        while self.visitCondition(ctx.getChild(2)):
            self.visitBlock_statement(ctx.getChild(4))

    # Visit a parse tree produced by MiniLangParser#print.
    def visitPrint(self, ctx: MiniLangParser.PrintContext):
        if len(self.output) >= self.output_limit:
            raise OutputLimitExceededException("Przekroczono limit wyjścia")
        self.output.append(self.visitExpression(ctx.getChild(2)))

    # Visit a parse tree produced by MiniLangParser#var.
    def visitVar(self, ctx: MiniLangParser.VarContext):
        variable_name = ctx.getText()
        if variable_name not in self.variables:
            self.variables[variable_name] = self.get_next_input()
        return self.variables[variable_name]

    # Visit a parse tree produced by MiniLangParser#integer.
    def visitInteger(self, ctx: MiniLangParser.IntegerContext):
        return int(ctx.getText())

    # Visit a parse tree produced by MiniLangParser#boolean.
    def visitBoolean(self, ctx: MiniLangParser.BooleanContext):
        return ctx.getText() == 'True'


del MiniLangParser
