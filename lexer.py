from ply import lex
import ply.yacc as yacc

tokens = (
    'LETTERS',
    'NEGATIVE',
    'AND',
    'OR',
    'IMPLICATION',
    'DIMPLICATION',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'CONST'
)

t_ignore = ' \t'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LETTERS = r'[p-z]'
t_CONST = r'[0-1]'
t_COMMA = r'\,'
t_AND = r'\^'
t_OR = r'o'
t_NEGATIVE = r'\~'
t_IMPLICATION = r'\=>'
t_DIMPLICATION = r'\<=>'

def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )


lexer = lex.lex()

precedence = (
    ('left', 'OR' ),
    ( 'left', 'AND' ),
    ( 'left', 'NEGATIVE' ),
)




def p_neg3( p ) :
    'expr : LETTERS'
    p[0] = p[1]

def p_neg2( p ) :
    'expr : NEGATIVE expr'
    p[0] = p[2]

def p_par(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_andexp(p):
    'expr : expr AND expr'
    p[0] = p[2]

def p_orexp(p):
    'expr : expr OR expr'
    p[0] = p[2]

def p_impli(p):
    'expr : expr IMPLICATION expr'
    p[0] = p[2]

def p_dimpli(p):
    'expr : expr DIMPLICATION expr'
    p[0] = p[2]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

res = parser.parse("((p=>q)^p)")
print(res)