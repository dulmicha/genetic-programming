grammar MiniLang;


program          : instruction*;

instruction      : loop
                 | if
                 | assignment
                 | print;

if               : 'if' '(' condition ')' block_statement;

condition        : condition_body (logical_operation = ('and' | 'or') condition_body)*;

condition_body    : expression comparison_operator = ('>' | '<' | '==' | '!=' | '<=' | '>=') (expression | boolean);

input            : 'input()';

assignment       : var '=' (expression | input) ';';

expression       : variable_name = var
                 | number = integer
                 | math_ex = math_expression;

math_expression  : '(' expression arithmetic_operator = ('+' | '-' | '/' | '*') expression ')';

block_statement  : '{' instruction* '}';

loop             : 'for' nonzero_digit block_statement;

print            : 'print' '(' expression ')' ';';

var               : VAR_NAME;

nonzero_digit     : POSITIVE_INT;

integer           : INT | POSITIVE_INT;

boolean           : 'True' | 'False';

POSITIVE_INT      : [1-9][0-9]*;

INT               : ('-')? POSITIVE_INT | '0';

VAR_NAME          : 'X_' [0-9]+;

WS                : [ \t\r\n]+ -> skip;
