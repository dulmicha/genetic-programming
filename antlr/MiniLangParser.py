# Generated from C:/Users/wehil/PycharmProjects/genetic-programming/antlr/MiniLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,121,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,55,
        8,2,10,2,12,2,58,9,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,67,8,3,1,4,
        1,4,1,5,1,5,1,5,1,5,3,5,75,8,5,1,5,1,5,1,6,1,6,1,6,3,6,82,8,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,5,8,92,8,8,10,8,12,8,95,9,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,
        13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,0,0,18,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,0,4,1,0,12,17,1,0,18,21,1,
        0,22,23,1,0,24,25,112,0,39,1,0,0,0,2,46,1,0,0,0,4,48,1,0,0,0,6,62,
        1,0,0,0,8,68,1,0,0,0,10,70,1,0,0,0,12,81,1,0,0,0,14,83,1,0,0,0,16,
        89,1,0,0,0,18,98,1,0,0,0,20,102,1,0,0,0,22,106,1,0,0,0,24,108,1,
        0,0,0,26,110,1,0,0,0,28,112,1,0,0,0,30,114,1,0,0,0,32,116,1,0,0,
        0,34,118,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,
        1,0,0,0,39,40,1,0,0,0,40,1,1,0,0,0,41,39,1,0,0,0,42,47,3,18,9,0,
        43,47,3,4,2,0,44,47,3,10,5,0,45,47,3,20,10,0,46,42,1,0,0,0,46,43,
        1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,49,5,1,0,0,49,
        50,5,2,0,0,50,56,3,6,3,0,51,52,3,26,13,0,52,53,3,6,3,0,53,55,1,0,
        0,0,54,51,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,
        1,0,0,0,58,56,1,0,0,0,59,60,5,3,0,0,60,61,3,16,8,0,61,5,1,0,0,0,
        62,63,3,12,6,0,63,66,3,22,11,0,64,67,3,12,6,0,65,67,3,34,17,0,66,
        64,1,0,0,0,66,65,1,0,0,0,67,7,1,0,0,0,68,69,5,4,0,0,69,9,1,0,0,0,
        70,71,3,28,14,0,71,74,5,5,0,0,72,75,3,12,6,0,73,75,3,8,4,0,74,72,
        1,0,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,77,5,6,0,0,77,11,1,0,0,0,
        78,82,3,28,14,0,79,82,3,32,16,0,80,82,3,14,7,0,81,78,1,0,0,0,81,
        79,1,0,0,0,81,80,1,0,0,0,82,13,1,0,0,0,83,84,5,2,0,0,84,85,3,12,
        6,0,85,86,3,24,12,0,86,87,3,12,6,0,87,88,5,3,0,0,88,15,1,0,0,0,89,
        93,5,7,0,0,90,92,3,2,1,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,
        0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,8,0,0,97,17,
        1,0,0,0,98,99,5,9,0,0,99,100,3,30,15,0,100,101,3,16,8,0,101,19,1,
        0,0,0,102,103,5,10,0,0,103,104,3,12,6,0,104,105,5,11,0,0,105,21,
        1,0,0,0,106,107,7,0,0,0,107,23,1,0,0,0,108,109,7,1,0,0,109,25,1,
        0,0,0,110,111,7,2,0,0,111,27,1,0,0,0,112,113,5,28,0,0,113,29,1,0,
        0,0,114,115,5,26,0,0,115,31,1,0,0,0,116,117,5,27,0,0,117,33,1,0,
        0,0,118,119,7,3,0,0,119,35,1,0,0,0,7,39,46,56,66,74,81,93
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'input()'", "'='", 
                     "';'", "'{'", "'}'", "'for'", "'print('", "');'", "'>'", 
                     "'<'", "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'and'", "'or'", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "POSITIVE_INT", "INT", "VAR_NAME", 
                      "WS" ]

    RULE_program = 0
    RULE_instruction = 1
    RULE_if = 2
    RULE_condition = 3
    RULE_input = 4
    RULE_assignment = 5
    RULE_expression = 6
    RULE_math_expression = 7
    RULE_block_statement = 8
    RULE_loop = 9
    RULE_print = 10
    RULE_comparison_operator = 11
    RULE_arithmetic_operator = 12
    RULE_logical_operation = 13
    RULE_var = 14
    RULE_nonzero_digit = 15
    RULE_integer = 16
    RULE_boolean = 17

    ruleNames =  [ "program", "instruction", "if", "condition", "input", 
                   "assignment", "expression", "math_expression", "block_statement", 
                   "loop", "print", "comparison_operator", "arithmetic_operator", 
                   "logical_operation", "var", "nonzero_digit", "integer", 
                   "boolean" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    POSITIVE_INT=26
    INT=27
    VAR_NAME=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.InstructionContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268436994) != 0):
                self.state = 36
                self.instruction()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop(self):
            return self.getTypedRuleContext(MiniLangParser.LoopContext,0)


        def if_(self):
            return self.getTypedRuleContext(MiniLangParser.IfContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniLangParser.AssignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(MiniLangParser.PrintContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = MiniLangParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.loop()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.if_()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.assignment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.print_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ConditionContext,i)


        def block_statement(self):
            return self.getTypedRuleContext(MiniLangParser.Block_statementContext,0)


        def logical_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.Logical_operationContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.Logical_operationContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = MiniLangParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MiniLangParser.T__0)
            self.state = 49
            self.match(MiniLangParser.T__1)
            self.state = 50
            self.condition()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 51
                self.logical_operation()
                self.state = 52
                self.condition()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(MiniLangParser.T__2)
            self.state = 60
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpressionContext,i)


        def comparison_operator(self):
            return self.getTypedRuleContext(MiniLangParser.Comparison_operatorContext,0)


        def boolean(self):
            return self.getTypedRuleContext(MiniLangParser.BooleanContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.expression()
            self.state = 63
            self.comparison_operator()
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 27, 28]:
                self.state = 64
                self.expression()
                pass
            elif token in [24, 25]:
                self.state = 65
                self.boolean()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = MiniLangParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MiniLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(MiniLangParser.VarContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def input_(self):
            return self.getTypedRuleContext(MiniLangParser.InputContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.var()
            self.state = 71
            self.match(MiniLangParser.T__4)
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 27, 28]:
                self.state = 72
                self.expression()
                pass
            elif token in [4]:
                self.state = 73
                self.input_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 76
            self.match(MiniLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(MiniLangParser.VarContext,0)


        def integer(self):
            return self.getTypedRuleContext(MiniLangParser.IntegerContext,0)


        def math_expression(self):
            return self.getTypedRuleContext(MiniLangParser.Math_expressionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.var()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.integer()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.math_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpressionContext,i)


        def arithmetic_operator(self):
            return self.getTypedRuleContext(MiniLangParser.Arithmetic_operatorContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_math_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expression" ):
                listener.enterMath_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expression" ):
                listener.exitMath_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expression" ):
                return visitor.visitMath_expression(self)
            else:
                return visitor.visitChildren(self)




    def math_expression(self):

        localctx = MiniLangParser.Math_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_math_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MiniLangParser.T__1)
            self.state = 84
            self.expression()
            self.state = 85
            self.arithmetic_operator()
            self.state = 86
            self.expression()
            self.state = 87
            self.match(MiniLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.InstructionContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_block_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_statement" ):
                listener.enterBlock_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_statement" ):
                listener.exitBlock_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MiniLangParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MiniLangParser.T__6)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268436994) != 0):
                self.state = 90
                self.instruction()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(MiniLangParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonzero_digit(self):
            return self.getTypedRuleContext(MiniLangParser.Nonzero_digitContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MiniLangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MiniLangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MiniLangParser.T__8)
            self.state = 99
            self.nonzero_digit()
            self.state = 100
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = MiniLangParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MiniLangParser.T__9)
            self.state = 103
            self.expression()
            self.state = 104
            self.match(MiniLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_comparison_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_operator" ):
                listener.enterComparison_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_operator" ):
                listener.exitComparison_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_operator" ):
                return visitor.visitComparison_operator(self)
            else:
                return visitor.visitChildren(self)




    def comparison_operator(self):

        localctx = MiniLangParser.Comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_arithmetic_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_operator" ):
                listener.enterArithmetic_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_operator" ):
                listener.exitArithmetic_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_operator" ):
                return visitor.visitArithmetic_operator(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_operator(self):

        localctx = MiniLangParser.Arithmetic_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arithmetic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_logical_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_operation" ):
                listener.enterLogical_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_operation" ):
                listener.exitLogical_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_operation" ):
                return visitor.visitLogical_operation(self)
            else:
                return visitor.visitChildren(self)




    def logical_operation(self):

        localctx = MiniLangParser.Logical_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logical_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(MiniLangParser.VAR_NAME, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MiniLangParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MiniLangParser.VAR_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nonzero_digitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITIVE_INT(self):
            return self.getToken(MiniLangParser.POSITIVE_INT, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_nonzero_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonzero_digit" ):
                listener.enterNonzero_digit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonzero_digit" ):
                listener.exitNonzero_digit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonzero_digit" ):
                return visitor.visitNonzero_digit(self)
            else:
                return visitor.visitChildren(self)




    def nonzero_digit(self):

        localctx = MiniLangParser.Nonzero_digitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nonzero_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MiniLangParser.POSITIVE_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = MiniLangParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MiniLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = MiniLangParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





