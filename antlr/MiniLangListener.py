# Generated from C:/Users/wehil/PycharmProjects/genetic-programming/antlr/MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#instruction.
    def enterInstruction(self, ctx:MiniLangParser.InstructionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#instruction.
    def exitInstruction(self, ctx:MiniLangParser.InstructionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#if.
    def enterIf(self, ctx:MiniLangParser.IfContext):
        pass

    # Exit a parse tree produced by MiniLangParser#if.
    def exitIf(self, ctx:MiniLangParser.IfContext):
        pass


    # Enter a parse tree produced by MiniLangParser#condition.
    def enterCondition(self, ctx:MiniLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#condition.
    def exitCondition(self, ctx:MiniLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#input.
    def enterInput(self, ctx:MiniLangParser.InputContext):
        pass

    # Exit a parse tree produced by MiniLangParser#input.
    def exitInput(self, ctx:MiniLangParser.InputContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assignment.
    def enterAssignment(self, ctx:MiniLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assignment.
    def exitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expression.
    def enterExpression(self, ctx:MiniLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expression.
    def exitExpression(self, ctx:MiniLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#math_expression.
    def enterMath_expression(self, ctx:MiniLangParser.Math_expressionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#math_expression.
    def exitMath_expression(self, ctx:MiniLangParser.Math_expressionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#block_statement.
    def enterBlock_statement(self, ctx:MiniLangParser.Block_statementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#block_statement.
    def exitBlock_statement(self, ctx:MiniLangParser.Block_statementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#loop.
    def enterLoop(self, ctx:MiniLangParser.LoopContext):
        pass

    # Exit a parse tree produced by MiniLangParser#loop.
    def exitLoop(self, ctx:MiniLangParser.LoopContext):
        pass


    # Enter a parse tree produced by MiniLangParser#print.
    def enterPrint(self, ctx:MiniLangParser.PrintContext):
        pass

    # Exit a parse tree produced by MiniLangParser#print.
    def exitPrint(self, ctx:MiniLangParser.PrintContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comparison_operator.
    def enterComparison_operator(self, ctx:MiniLangParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comparison_operator.
    def exitComparison_operator(self, ctx:MiniLangParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by MiniLangParser#arithmetic_operator.
    def enterArithmetic_operator(self, ctx:MiniLangParser.Arithmetic_operatorContext):
        pass

    # Exit a parse tree produced by MiniLangParser#arithmetic_operator.
    def exitArithmetic_operator(self, ctx:MiniLangParser.Arithmetic_operatorContext):
        pass


    # Enter a parse tree produced by MiniLangParser#logical_operation.
    def enterLogical_operation(self, ctx:MiniLangParser.Logical_operationContext):
        pass

    # Exit a parse tree produced by MiniLangParser#logical_operation.
    def exitLogical_operation(self, ctx:MiniLangParser.Logical_operationContext):
        pass


    # Enter a parse tree produced by MiniLangParser#var.
    def enterVar(self, ctx:MiniLangParser.VarContext):
        pass

    # Exit a parse tree produced by MiniLangParser#var.
    def exitVar(self, ctx:MiniLangParser.VarContext):
        pass


    # Enter a parse tree produced by MiniLangParser#nonzero_digit.
    def enterNonzero_digit(self, ctx:MiniLangParser.Nonzero_digitContext):
        pass

    # Exit a parse tree produced by MiniLangParser#nonzero_digit.
    def exitNonzero_digit(self, ctx:MiniLangParser.Nonzero_digitContext):
        pass


    # Enter a parse tree produced by MiniLangParser#integer.
    def enterInteger(self, ctx:MiniLangParser.IntegerContext):
        pass

    # Exit a parse tree produced by MiniLangParser#integer.
    def exitInteger(self, ctx:MiniLangParser.IntegerContext):
        pass


    # Enter a parse tree produced by MiniLangParser#boolean.
    def enterBoolean(self, ctx:MiniLangParser.BooleanContext):
        pass

    # Exit a parse tree produced by MiniLangParser#boolean.
    def exitBoolean(self, ctx:MiniLangParser.BooleanContext):
        pass



del MiniLangParser