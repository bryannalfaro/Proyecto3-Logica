from ply import lex
import ply.yacc as yacc
import networkx as nx
import matplotlib.pyplot as plt

contador = {
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
}

contadorSymbols = {}
operators = ['o','^','~','=>','<=>']
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
    ( 'left', 'IMPLICATION' ),
    ( 'left', 'NEGATIVE' ),

)

def p_neg3( p ) :
    'expr : LETTERS'
    print(p[1])
    print(exp)
    if exp.find('o') == -1 and exp.find('^') == -1 and exp.find('=>') == -1 and exp.find('<=>') == -1:
        g.add_node(p[1])
    print(contador[p[1]])


    p[0] = p[1]

def p_neg2( p ) :
    'expr : NEGATIVE expr'
    # g.add_edge( p[1], p[2])
    # print(p[1], 'neg' , p[2])
    simbol =  p[1]
    find = True
    print(p[2])
    # print(list(g.nodes()), 'desde or')
    # print(p[2] in list(g.nodes()))
    while find:
        if simbol in list(g.nodes()):
            simbol = simbol + ' '
        else:
            find = False
    if p[2] in contador:
        contador[p[2]] += 1
        g.add_edge(simbol, p[2] + contador[p[2]] * ' ')
    elif p[2][0] in operators:
        g.add_edge(simbol, p[2][0])
    elif p[2][1] in operators:
        g.add_edge(p[1], p[2][1])
    elif p[2][1] + p[2][2] in operators:
        g.add_edge(p[1], p[2][1] + p[2][2])
    elif p[2][1] + p[2][2] + p[2][3] in operators:
        g.add_edge(p[1], p[2][1] + p[2][2] + p[2][3])
    # p[0] = p[1]+ p[2]
    p[0] = p[1]+ p[2]

def p_par(p):
    'expr : LPAREN expr RPAREN'
    #g.add_node(p[2])
    p[0] = p[2]

def p_andexp(p):
    'expr : expr AND expr'
    print(p[3],'p2 inicio and')
    simbol =  p[2]
    find = True
    # print(list(g.nodes()), 'desde or')
    # print(p[2] in list(g.nodes()))
    # print('ENTRO AL IF', p[1], ' ', p[1][1], ' ',p[1][1] in operators , p[2], ' ', p[3])
    while find:
        if simbol in list(g.nodes()):
            simbol = simbol + ' '
        else:
            find = False
    try: # siguiente simbolo esta del lado izquierdo
        if (p[1].find('~')) != -1:
            neg = p[1][0]
            g.add_edge(simbol,neg)
            g.add_edge(simbol,p[3])
        elif p[1][1] in operators:
            print("primer IF AND")
            if p[3] in contador:
                contador[p[3]] += 1
                # g.add_edge(p[2],p[3] + (contador[p[3]] * ' '))
                g.add_edge(simbol,p[3] + (contador[p[3]] * ' '))
            print(p[3] in contador)
            # g.add_edge(p[2],p[1][1])
            g.add_edge(simbol,p[1][1])
        elif p[1][1] + p[1][2] in operators:
            print("primer IF AND")
            if p[3] in contador:
                contador[p[3]] += 1
                # g.add_edge(p[2],p[3] + (contador[p[3]] * ' '))
                g.add_edge(simbol,p[3] + (contador[p[3]] * ' '))
            print(p[3] in contador)
            # g.add_edge(p[2],p[1][1])
            g.add_edge(simbol,p[1][1] + p[1][2])

    except:
        try: # cuando el siguiente simbolo estaba del lado derecho
            if p[3].find('~') != -1:
                neg = p[3][0]
                g.add_edge(simbol, p[1])
                g.add_edge(simbol, neg)
            elif p[3][1] in operators:

                print("segundo IF AND")
                print('AAAAAAAA')
                contador[p[1]] += 1
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1])
                # g.add_edge(p[2],p[1] + (contador[p[1]] * ' '))
                g.add_edge(simbol,p[3][1])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
            elif p[3][1] + p[3][2] in operators:
                print("segundo IF AND")
                print('EEEEEEE')
                contador[p[1]] += 1
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1] + p[3][2])
                # g.add_edge(p[2],p[1] + (contador[p[1]] * ' '))
                g.add_edge(simbol,p[3][1] + p[3][2])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
            elif p[3][1]+p[3][2] + p[3][3] in operators:
                print("entro doble impo")
                print('eerrrrrrr')
                contador[p[1]] += 1
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1] + p[3][2])
                # g.add_edge(p[2],p[1] + (contador[p[1]] * ' '))
                g.add_edge(simbol,p[3][1] + p[3][2]+p[3][3])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
        except:
                # g.add_edge(p[2],p[1] + (contador[p[1]] * ' '))
                contador[p[1]] += 1
                contador[p[3]] += 1
                print(contador,'ultimo except and')
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
                g.add_edge(simbol,p[3] + (contador[p[3]] * ' '))
                # g.add_edge(p[2],p[3] + (contador[p[3]] * ' '))

    p[0] = p[1]+p[2]+p[3]

def p_orexp(p):
    'expr : expr OR expr'

    #g.add_edge(p[2],p[1])
    simbol =  p[2]
    find = True
    # print(list(g.nodes()), 'desde or')
    # print(p[2] in list(g.nodes()))
    print('lista nodos',list(g.nodes()),simbol)
    while find:
        if simbol in list(g.nodes()):
            print('entro per')
            simbol = simbol + ' '
        else:
            find = False
    print(simbol,'simbol')
    try:
        if (p[1].find('~')) != -1:
            neg = p[1][0]
            g.add_edge(simbol,neg)
            g.add_edge(simbol,p[3])
        if p[1][1] in operators:
            print(p[3] in contador,'primer if or')
            contador[p[3]] += 1
            print(contador, "primer if OR")
            new = p[3] + (contador[p[3]] * ' ')
            # g.add_edge(p[2],p[1][1])
            # g.add_edge(p[2], new)
            g.add_edge(simbol,p[1][1])
            g.add_edge(simbol, new)
            print(contador[p[3]])
        elif p[1][1] + p[1][2] in operators:
            print(p[3] in contador,'primer if or')
            contador[p[3]] += 1
            print(contador, "primer if OR")
            new = p[3] + (contador[p[3]] * ' ')
            # g.add_edge(p[2],p[1][1])
            # g.add_edge(p[2], new)
            g.add_edge(simbol,p[1][1] + p[1][2])
            g.add_edge(simbol, new)
            print(contador[p[3]])
    except:
        try:
            if p[3].find('~') != -1:
                neg = p[3][0]
                g.add_edge(simbol, p[1])
                g.add_edge(simbol, neg)
            if p[3][1] in operators:
                print("segundo IF OR")
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1])
                # g.add_edge(p[2],p[1] + (2 * ' '))
                contador[p[1]]+=1
                g.add_edge(simbol,p[3][1])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
            elif p[3][1] + p[3][2] in operators:
                print("segundo IF OR")
                print(p[3] in contador)
                contador[p[1]]+=1
                # g.add_edge(p[2],p[3][1])
                # g.add_edge(p[2],p[1] + (2 * ' '))
                g.add_edge(simbol,p[3][1] + p[3][2])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
        except:
                print("ultimo except OR")
                # g.add_edge(p[2],p[1]+' ')
                # g.add_edge(p[2],p[3])
                contador[p[1]] += 1
                contador[p[3]] += 1

                g.add_edge(simbol,p[1] + contador[p[1]] * ' ')
                g.add_edge(simbol,p[3] + contador[p[3]] * ' ')

    p[0] = p[1]+p[2]+p[3]


def p_impli(p):
    'expr : expr IMPLICATION expr'
    # g.add_edge(p[2],p[1]+' ')
    # g.add_edge(p[2],p[3]+' ')
    # g.add_edge(p[2]+' ',p[1]+p[2]+p[3])
    #g.add_edge(p[2],p[1])
    simbol =  p[2]
    find = True
    # print(list(g.nodes()), 'desde or')
    # print(p[2] in list(g.nodes()))
    while find:
        if simbol in list(g.nodes()):
            simbol = simbol + ' '
        else:
            find = False
    try:
        if p[1].find('~') != -1:
                neg = p[1][0]
                g.add_edge(simbol, p[3])
                print('neg izquierdo',neg,p[1],p[3],simbol)
                g.add_edge(simbol, neg)
        elif p[1][1] in operators:
            print("primer IF IMP")
            if p[3] in contador:
                contador[p[3]] += 1
                # g.add_edge(p[2],p[3] + (contador[p[3]] * ' '))
                g.add_edge(simbol,p[3] + (contador[p[3]] * ' '))
            print(p[3] in contador)
            # g.add_edge(p[2],p[1][1])
            g.add_edge(simbol,p[1][1])
        elif p[1][1] + p[1][2] in operators:
            print(p[3] in contador,'primer if IMP')
            contador[p[3]] += 1
            print(contador, "primer if IMP")
            new = p[3] + (contador[p[3]] * ' ')
            # g.add_edge(p[2],p[1][1])
            # g.add_edge(p[2], new)
            g.add_edge(simbol,p[1][1] + p[1][2])
            g.add_edge(simbol, new)
            print(contador[p[3]])
    except:
        try:
            if p[3].find('~') != -1:
                neg = p[3][0]
                g.add_edge(simbol, p[1])

                g.add_edge(simbol, neg)
            elif p[3][1] in operators:
                print("segundo IF IMP")
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1])
                # g.add_edge(p[2],p[1] + (2 * ' '))
                g.add_edge(simbol,p[3][1])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
            elif p[3][1] + p[3][2] in operators:
                print("segundo IF IMP")
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1])
                # g.add_edge(p[2],p[1] + (2 * ' '))
                g.add_edge(simbol,p[3][1] + p[3][2])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
        except:
                print("ultimo except IMP")
                # g.add_edge(p[2],p[1]+' ')
                # g.add_edge(p[2],p[3])
                # print(contador[p[1]])
                # print(contador[p[3]])
                contador[p[1]] += 1
                contador[p[3]] += 1
                g.add_edge(simbol,p[1] + contador[p[1]] * ' ')
                g.add_edge(simbol,p[3] + contador[p[3]] * ' ')

    p[0] = p[1]+p[2]+p[3]

def p_dimpli(p):
    'expr : expr DIMPLICATION expr'
    # g.add_edge(p[2],p[1])
    # g.add_edge(p[2],p[3])
    simbol =  p[2]
    find = True
    # print(list(g.nodes()), 'desde or')
    # print(p[2] in list(g.nodes()))
    while find:
        if simbol in list(g.nodes()):
            simbol = simbol + ' '
        else:
            find = False
    try:
        if p[1].find('~') != -1:
                neg = p[1][0]
                g.add_edge(simbol, p[3])
                print('neg izquierdo',neg,p[1],p[3],simbol)
                g.add_edge(simbol, neg)
        elif p[1][1] in operators:
            print("primer IF IMP")
            if p[3] in contador:
                contador[p[3]] += 1
                # g.add_edge(p[2],p[3] + (contador[p[3]] * ' '))
                g.add_edge(simbol,p[3] + (contador[p[3]] * ' '))
            print(p[3] in contador)
            # g.add_edge(p[2],p[1][1])
            g.add_edge(simbol,p[1][1])
        elif p[1][1] + p[1][2] in operators:
            print(p[3] in contador,'primer if IMP')
            contador[p[3]] += 1
            print(contador, "primer if IMP")
            new = p[3] + (contador[p[3]] * ' ')
            # g.add_edge(p[2],p[1][1])
            # g.add_edge(p[2], new)
            g.add_edge(simbol,p[1][1] + p[1][2])
            g.add_edge(simbol, new)
            print(contador[p[3]])
    except:
        try:
            if p[3].find('~') != -1:
                neg = p[3][0]
                g.add_edge(simbol, p[1])

                g.add_edge(simbol, neg)
            elif p[3][1] in operators:
                print("segundo IF IMP")
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1])
                # g.add_edge(p[2],p[1] + (2 * ' '))
                g.add_edge(simbol,p[3][1])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
            elif p[3][1] + p[3][2] in operators:
                print("segundo IF IMP")
                print(p[3] in contador)
                # g.add_edge(p[2],p[3][1])
                # g.add_edge(p[2],p[1] + (2 * ' '))
                g.add_edge(simbol,p[3][1] + p[3][2])
                g.add_edge(simbol,p[1] + (contador[p[1]] * ' '))
        except:
                print("ultimo except IMP")
                # g.add_edge(p[2],p[1]+' ')
                # g.add_edge(p[2],p[3])
                # print(contador[p[1]])
                # print(contador[p[3]])
                contador[p[1]] += 1
                contador[p[3]] += 1
                g.add_edge(simbol,p[1] + contador[p[1]] * ' ')
                g.add_edge(simbol,p[3] + contador[p[3]] * ' ')

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
    #g.add_node(p[1])
    print(contador,'const')
    p[0] = p[1]

def p_error( p ):
    print("Syntax error in input!")



parser = yacc.yacc()
global g
g = nx.Graph()

# doble imp

exp = '(p^(p<=>q))'
res = parser.parse(exp)
print(list(g.nodes()))



nx.draw(g, with_labels = True)
plt.savefig("filename.png")
print(res)