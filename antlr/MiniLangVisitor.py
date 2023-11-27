# Generated from C:/Users/wehil/PycharmProjects/genetic-programming/antlr/MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#instruction.
    def visitInstruction(self, ctx:MiniLangParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#if.
    def visitIf(self, ctx:MiniLangParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#condition.
    def visitCondition(self, ctx:MiniLangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#input.
    def visitInput(self, ctx:MiniLangParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assignment.
    def visitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expression.
    def visitExpression(self, ctx:MiniLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#math_expression.
    def visitMath_expression(self, ctx:MiniLangParser.Math_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block_statement.
    def visitBlock_statement(self, ctx:MiniLangParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#loop.
    def visitLoop(self, ctx:MiniLangParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#print.
    def visitPrint(self, ctx:MiniLangParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#comparison_operator.
    def visitComparison_operator(self, ctx:MiniLangParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#arithmetic_operator.
    def visitArithmetic_operator(self, ctx:MiniLangParser.Arithmetic_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#logical_operation.
    def visitLogical_operation(self, ctx:MiniLangParser.Logical_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#var.
    def visitVar(self, ctx:MiniLangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#nonzero_digit.
    def visitNonzero_digit(self, ctx:MiniLangParser.Nonzero_digitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#integer.
    def visitInteger(self, ctx:MiniLangParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#boolean.
    def visitBoolean(self, ctx:MiniLangParser.BooleanContext):
        return self.visitChildren(ctx)



del MiniLangParser