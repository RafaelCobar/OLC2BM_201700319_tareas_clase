
# ANALISIS LEXICO
tokens = (
    'Id',
    'Sumar',
    'Restar',
    'Multiplicar',
    'Dividir',
    'PI',
    'PD'
)

#Tokens
t_Sumar = r'\+'
t_Restar = r'-'
t_Multiplicar = r'\*'
t_Dividir = r'/'
t_PI = r'\('
t_PD = r'\)'

def t_Id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print("Error Léxico, Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)

#Caracteres ignorados
t_ignore = " \t"



import ply.lex as lex
lexer = lex.lex()


# Nuevo nodo
class NewNodo():
    def __init__(self, opIzq, signo, opDer):
        self.opIzq = opIzq
        self.opDer = opDer
        self.signo = signo


# Analisis Sintactico

def p_s(t):
    's : e'
    t[0] = t[1]

def p_e_e_sumar_t(t):
    'e    :   e Sumar t'
    t[0] = NewNodo(t[1], '+', t[3])
    
def p_e_e_restar_t(t):
    'e    :   e Restar t'
    t[0] = NewNodo(t[1], '-', t[3])
    
def p_e_e_t(t):
    'e    :   t'
    t[0] = t[1]
    
def p_t_t_mult_f(t):
    't    :   t Multiplicar f'
    t[0] = NewNodo(t[1], '*', t[3])
    
def p_t_t_div_f(t):
    't    :   t Dividir f'
    t[0] = NewNodo(t[1], '/', t[3])
    
def p_t_t_f(t):
    't    :   f'
    t[0] = t[1]
    
def p_f_parentesis(t):
    'f    :   PI e PD'
    t[0] = t[2]

def p_f_id(t):
    'f    :   Id'
    t[0] = t[1]



def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
