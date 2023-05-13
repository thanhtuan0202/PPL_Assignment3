//My student ID: 2014931
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declaration+ EOF;
declaration : vardecl | funcdecl;

vardecl: varlist DDOT (mt_type | AUTO) SEMI
		| varwithexprdecl SEMI ;
varlist: IDENTIFIER | varlist COMMA IDENTIFIER;

varwithexprdecl: varini | IDENTIFIER COMMA varwithexprdecl COMMA expr;
varini: IDENTIFIER DDOT (mt_type | AUTO) EQUAL expr;

funcdecl: IDENTIFIER DDOT FUNCTION return_type LB paralist? RB (inherit)? block_stmt ;
inherit: INHERIT IDENTIFIER;
return_type: mt_type | VOID | AUTO;
paralist: parameter | paralist COMMA parameter;
parameter: INHERIT? OUT? IDENTIFIER DDOT (mt_type | AUTO);
mt_type: atomic_type | array_type;
//statement
stmt: 
	assign_stmt 
	| if_stmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| break_stmt | return_stmt | continue_stmt
	| call_stmt 
	|block_stmt ;

//assign statement
assign_stmt: lhs EQUAL expr SEMI;
lhs: IDENTIFIER | index_op;
//if statement
//if_stmt: IF LB expr RB stmt (ELSE IF LB expr RB stmt)* (ELSE stmt)?;
if_stmt: fullif | halfif;
fullif: IF LB expr RB stmt ELSE stmt;
halfif: IF LB expr RB stmt 
		| IF LB expr RB (fullif|stmt) ELSE halfif;
//for statement
for_stmt: FOR LB init_expr COMMA cond_expr COMMA update_expr RB stmt;
init_expr: IDENTIFIER EQUAL expr;
cond_expr: expr;
update_expr: expr;

//while statement
while_stmt: WHILE LB expr RB stmt;

//do while statment
do_while_stmt: DO block_stmt WHILE LB expr RB SEMI;

//return stmt
return_stmt: RETURN expr SEMI;
//call stmt
call_stmt: IDENTIFIER LB exprlist? RB SEMI;
exprlist: exprlist COMMA expr |  expr;

break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;

//block statement
block_stmt: LCB body RCB;
body:bodypara body | ;
bodypara: stmt | vardecl;
//expression

expr: expr SCOPE expr1 | expr1;
expr1: expr2  relational expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB )  expr4 | expr4;
expr4: expr4 mul_div expr5  | expr5;
expr5: NOT expr6 | expr6;
expr6: SUB expr7 | expr7;
expr7: operands;

operands: IDENTIFIER | literial | func_call | LB expr RB  | index_op;
literial: INTLIT | STRINGLIT | BOOLLIT | FLOATLIT | arraylit;
func_call: IDENTIFIER LB exprlist? RB;
index_op: IDENTIFIER LSB exprlist RSB;

mul_div: MUL | DIV | MOD;
relational: EQUALTO | NOTEQ | LESS | GREAT | GREATEQ | LESSEQ;
//type and values
//atomic type
atomic_type: FLOAT | INTEGER | STRING | BOOLEAN ;
//array type
array_type: ARRAY LSB intlist RSB OF  (atomic_type | AUTO);
intlist: INTLIT | intlist COMMA INTLIT;

arraylit: arraylit_para | LCB arraylitlist RCB;
arraylitlist: arraylit_para | arraylitlist COMMA arraylit_para ;
arraylit_para: LCB exprlist? RCB;
// Skip comments

BLOCK_COMMENT: ('/*' .*? '*/') -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
//Literal:
INTLIT: '0' | ([1-9] [0-9]*) | ([1-9] ([0-9]* '_' [0-9]+)*) {self.text = self.text.replace("_", "")} ;
INLIT_ERROR_0: '0' [_0-9]+ {raise ErrorToken("0")} ;

FLOATLIT: ((INT_PART DEC_PART) | (INT_PART DEC_PART? EXP_PART)) {self.text = self.text.replace("_", "")};
fragment INT_PART: '0' | ([1-9] [0-9]*) | ([1-9] ([0-9]* '_'? [0-9]+)*);
fragment DEC_PART: '.' ([0-9]* | [0-9]+ ('_'? [0-9]+)* | );
fragment EXP_PART: ('e' | 'E') ('+' | '-')? ([0-9]+ | [0-9]+ ('_'? [0-9]+)*);

BOOLLIT: TRUE | FALSE;
STRINGLIT: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;
//keyword: 
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
//seperator:
EQUAL: '=';
SEMI: ';';
COMMA: ','; 
LB: '('; RB: ')';
LCB: '{';RCB: '}';
LSB: '['; RSB: ']';
DOT: '.';
DDOT: ':';

//operator:
ADD: '+'; SUB: '-'; MUL: '*';DIV: '/';MOD: '%';
NOT: '!'; AND: '&&'; OR: '||';EQUALTO: '==';
NOTEQ: '!=';
GREAT: '>'; LESS: '<';
GREATEQ: '>='; LESSEQ: '<=';
SCOPE: '::';
IDENTIFIER: [_a-zA-Z][_a-zA-Z0-9]*;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f]+ -> skip ; 


UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\ ]| EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\', '\\"']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	| '"' STR_CHAR* '\\"' STR_CHAR* { raise UncloseString(self.text)}
	;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;