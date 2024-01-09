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
        4,1,28,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,1,1,1,1,1,
        1,1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,54,8,3,10,
        3,12,3,57,9,3,1,4,1,4,1,4,1,4,3,4,63,8,4,1,5,1,5,1,6,1,6,1,6,1,6,
        3,6,71,8,6,1,6,1,6,1,7,1,7,1,7,3,7,78,8,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,9,1,9,5,9,88,8,9,10,9,12,9,91,9,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,
        1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,5,
        1,0,4,5,1,0,6,11,1,0,15,18,1,0,25,26,1,0,23,24,106,0,35,1,0,0,0,
        2,42,1,0,0,0,4,44,1,0,0,0,6,50,1,0,0,0,8,58,1,0,0,0,10,64,1,0,0,
        0,12,66,1,0,0,0,14,77,1,0,0,0,16,79,1,0,0,0,18,85,1,0,0,0,20,94,
        1,0,0,0,22,98,1,0,0,0,24,104,1,0,0,0,26,106,1,0,0,0,28,108,1,0,0,
        0,30,110,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,1,1,0,0,0,37,35,1,0,0,0,38,43,3,20,10,0,
        39,43,3,4,2,0,40,43,3,12,6,0,41,43,3,22,11,0,42,38,1,0,0,0,42,39,
        1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,3,1,0,0,0,44,45,5,1,0,0,45,
        46,5,2,0,0,46,47,3,6,3,0,47,48,5,3,0,0,48,49,3,18,9,0,49,5,1,0,0,
        0,50,55,3,8,4,0,51,52,7,0,0,0,52,54,3,8,4,0,53,51,1,0,0,0,54,57,
        1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,7,1,0,0,0,57,55,1,0,0,0,58,
        59,3,14,7,0,59,62,7,1,0,0,60,63,3,14,7,0,61,63,3,30,15,0,62,60,1,
        0,0,0,62,61,1,0,0,0,63,9,1,0,0,0,64,65,5,12,0,0,65,11,1,0,0,0,66,
        67,3,24,12,0,67,70,5,13,0,0,68,71,3,14,7,0,69,71,3,10,5,0,70,68,
        1,0,0,0,70,69,1,0,0,0,71,72,1,0,0,0,72,73,5,14,0,0,73,13,1,0,0,0,
        74,78,3,24,12,0,75,78,3,28,14,0,76,78,3,16,8,0,77,74,1,0,0,0,77,
        75,1,0,0,0,77,76,1,0,0,0,78,15,1,0,0,0,79,80,5,2,0,0,80,81,3,14,
        7,0,81,82,7,2,0,0,82,83,3,14,7,0,83,84,5,3,0,0,84,17,1,0,0,0,85,
        89,5,19,0,0,86,88,3,2,1,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,
        0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,20,0,0,93,
        19,1,0,0,0,94,95,5,21,0,0,95,96,3,26,13,0,96,97,3,18,9,0,97,21,1,
        0,0,0,98,99,5,22,0,0,99,100,5,2,0,0,100,101,3,14,7,0,101,102,5,3,
        0,0,102,103,5,14,0,0,103,23,1,0,0,0,104,105,5,27,0,0,105,25,1,0,
        0,0,106,107,5,25,0,0,107,27,1,0,0,0,108,109,7,3,0,0,109,29,1,0,0,
        0,110,111,7,4,0,0,111,31,1,0,0,0,7,35,42,55,62,70,77,89
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'and'", "'or'", 
                     "'>'", "'<'", "'=='", "'!='", "'<='", "'>='", "'input()'", 
                     "'='", "';'", "'+'", "'-'", "'/'", "'*'", "'{'", "'}'", 
                     "'for'", "'print'", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "POSITIVE_INT", "INT", "VAR_NAME", "WS" ]

    RULE_program = 0
    RULE_instruction = 1
    RULE_if = 2
    RULE_condition = 3
    RULE_condition_body = 4
    RULE_input = 5
    RULE_assignment = 6
    RULE_expression = 7
    RULE_math_expression = 8
    RULE_block_statement = 9
    RULE_loop = 10
    RULE_print = 11
    RULE_var = 12
    RULE_nonzero_digit = 13
    RULE_integer = 14
    RULE_boolean = 15

    ruleNames =  [ "program", "instruction", "if", "condition", "condition_body", 
                   "input", "assignment", "expression", "math_expression", 
                   "block_statement", "loop", "print", "var", "nonzero_digit", 
                   "integer", "boolean" ]

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
    POSITIVE_INT=25
    INT=26
    VAR_NAME=27
    WS=28

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140509186) != 0):
                self.state = 32
                self.instruction()
                self.state = 37
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
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.loop()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.if_()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.assignment()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
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

        def condition(self):
            return self.getTypedRuleContext(MiniLangParser.ConditionContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MiniLangParser.Block_statementContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MiniLangParser.T__0)
            self.state = 45
            self.match(MiniLangParser.T__1)
            self.state = 46
            self.condition()
            self.state = 47
            self.match(MiniLangParser.T__2)
            self.state = 48
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
            self.logical_operation = None # Token

        def condition_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.Condition_bodyContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.Condition_bodyContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.condition_body()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 51
                localctx.logical_operation = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    localctx.logical_operation = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.condition_body()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.comparison_operator = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpressionContext,i)


        def boolean(self):
            return self.getTypedRuleContext(MiniLangParser.BooleanContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_condition_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_body" ):
                listener.enterCondition_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_body" ):
                listener.exitCondition_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_body" ):
                return visitor.visitCondition_body(self)
            else:
                return visitor.visitChildren(self)




    def condition_body(self):

        localctx = MiniLangParser.Condition_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.expression()
            self.state = 59
            localctx.comparison_operator = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                localctx.comparison_operator = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 25, 26, 27]:
                self.state = 60
                self.expression()
                pass
            elif token in [23, 24]:
                self.state = 61
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
        self.enterRule(localctx, 10, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiniLangParser.T__11)
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
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.var()
            self.state = 67
            self.match(MiniLangParser.T__12)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 25, 26, 27]:
                self.state = 68
                self.expression()
                pass
            elif token in [12]:
                self.state = 69
                self.input_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 72
            self.match(MiniLangParser.T__13)
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
            self.variable_name = None # VarContext
            self.number = None # IntegerContext
            self.math_ex = None # Math_expressionContext

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
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                localctx.variable_name = self.var()
                pass
            elif token in [25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                localctx.number = self.integer()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                localctx.math_ex = self.math_expression()
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
            self.arithmetic_operator = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpressionContext,i)


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
        self.enterRule(localctx, 16, self.RULE_math_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MiniLangParser.T__1)
            self.state = 80
            self.expression()
            self.state = 81
            localctx.arithmetic_operator = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                localctx.arithmetic_operator = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 82
            self.expression()
            self.state = 83
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
        self.enterRule(localctx, 18, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MiniLangParser.T__18)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140509186) != 0):
                self.state = 86
                self.instruction()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(MiniLangParser.T__19)
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
        self.enterRule(localctx, 20, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MiniLangParser.T__20)
            self.state = 95
            self.nonzero_digit()
            self.state = 96
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
        self.enterRule(localctx, 22, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MiniLangParser.T__21)
            self.state = 99
            self.match(MiniLangParser.T__1)
            self.state = 100
            self.expression()
            self.state = 101
            self.match(MiniLangParser.T__2)
            self.state = 102
            self.match(MiniLangParser.T__13)
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
        self.enterRule(localctx, 24, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
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
        self.enterRule(localctx, 26, self.RULE_nonzero_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
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

        def POSITIVE_INT(self):
            return self.getToken(MiniLangParser.POSITIVE_INT, 0)

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
        self.enterRule(localctx, 28, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
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
        self.enterRule(localctx, 30, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
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





