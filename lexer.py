from ply import lex
import ply.yacc as yacc
import networkx as nx
import matplotlib.pyplot as plt



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
    ( 'left', 'IMPLICATION' ),
    ( 'left', 'AND' ),
    ( 'left', 'NEGATIVE' ),

)

def p_neg3( p ) :
    'expr : LETTERS'
    g.add_node(p[1])
    p[0] = p[1]

def p_neg2( p ) :
    'expr : NEGATIVE expr'
    g.add_edge( p[1], p[2])
    p[0] = p[1]+p[2]

def p_par(p):
    'expr : LPAREN expr RPAREN'
    g.add_node(p[2])
    p[0] = p[2]

def p_andexp(p):
    'expr : expr AND expr'

    g.add_edge(p[2],p[1])
    g.add_edge(p[2],p[3])
    g.add_edge(p[3],p[1]+p[2]+p[3])
    g.add_edge(p[1],p[1]+p[2]+p[3])
    p[0] = p[1]+p[2]+p[3]

def p_orexp(p):
    'expr : expr OR expr'

    g.add_edge(p[2],p[1])
    g.add_edge(p[2],p[3])
    p[0] = p[1]+p[2]+p[3]
    p[0] = p[1]+p[2]+p[3]

def p_impli(p):
    'expr : expr IMPLICATION expr'
    g.add_edge(p[2],p[1]+' ')
    g.add_edge(p[2],p[3]+' ')
    g.add_edge(p[2]+' ',p[1]+p[2]+p[3])
    p[0] = p[1]+p[2]+p[3]

def p_dimpli(p):
    'expr : expr DIMPLICATION expr'
    g.add_edge(p[2],p[1])
    g.add_edge(p[2],p[3])
    p[0] = p[1]+p[2]+p[3]

def p_comma(p):
    'expr : expr COMMA expr'
    g.add_edge(p[2],p[1])
    g.add_edge(p[2],p[3])
    p[0] = p[2]

def p_comma1(p):
    'expr : COMMA'
    g.add_node(p[1])
    p[0] = p[1]

def p_const(p):
    'expr : CONST'
    g.add_node(p[1])
    p[0] = p[1]

def p_error( p ):
    print("Syntax error in input!")



parser = yacc.yacc()
global g
g = nx.Graph()

res = parser.parse("((p=>q)^p)")
print(list(g.nodes()))



nx.draw(g, with_labels = True)
plt.savefig("filename.png")
print(res)