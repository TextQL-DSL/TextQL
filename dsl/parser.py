from ply.yacc import yacc, yaccdebug
from dsl.ast import *
from dsl.lexer import Lexer

lexer = Lexer()
lexer.build()
tokens = lexer.tokens

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV')
)

#--------------
def p_script(p):
    '''script : USE PDF STRING SEMICOLON statement
              | USE DOC STRING SEMICOLON statement
              | USE PDF STRING SEMICOLON
              | USE DOC STRING SEMICOLON'''
    
    doc_ext = DocExtension(p[2])
    path = String(p[3])
    Use(path, doc_ext)

    if(len(p) == 6):
        p[0] = p[5]

def p_statement(p):
    '''statement : query SEMICOLON statement 
                 | define SEMICOLON statement
                 | empty'''
    
    if(len(p) == 2):
        p[0] == p[1]
    
    else:
        p[0] = (p[1], p[3])


def p_define(p):
    '''define : DEFINE TYPE_STRING ID ASSIGN STRING
              | DEFINE TYPE_BOOLEAN ID ASSIGN boolean_expression
              | DEFINE TYPE_NUMBER ID ASSIGN arithmetic_expression'''
    
    Define(p[2], p[3], p[5])

def p_query(p):
    '''query : QUERY function'''
    
    p[0] = p[2]


def p_function(p):
    '''function : justword_func function
                | length_func function
                | touppercase_func function
                | slice_func function
                | empty'''
    
    if(len(p) == 2):
        p[0] = 1
    
    else:
        p[0] = (p[1], p(2))


# Binary Expressions
def p_arithmetic_expression(p):
    '''arithmetic_expression : arithmetic_expression ADD arithmetic_expression
                             | arithmetic_expression SUB arithmetic_expression
                             | arithmetic_expression MULT arithmetic_expression
                             | arithmetic_expression DIV arithmetic_expression
                             | numeric_complement
                             | NUMBER'''

    if(len(p) == 2):
        p[0] = p[1]
    
    elif(p[2] == 'ADD'):
        p[0] = p[1] + p[3]

    elif(p[2] == 'SUB'):
        p[0] = p[1] - p[3]

    elif(p[2] == 'MULT'):
        p[0] = p[1] * p[3]
    
    elif(p[2] == 'DIV'):
        p[0] = p[1] / p[3]

def p_boolean_expression(p):
    '''boolean_expression : boolean_expression EQ boolean_expression
                          | boolean_expression LE boolean_expression
                          | boolean_expression GR boolean_expression
                          | boolean_expression LEEQ boolean_expression
                          | boolean_expression GREQ boolean_expression
                          | boolean_complement
                          | BOOLEAN
                          | arithmetic_expression'''
    
    if(len(p) == 2):
        p[0] = p[1]
    
    elif(p[2] == 'EQ'):
        p[0] = p[1] == p[3]

    elif(p[2] == 'LE'):
        p[0] = p[1] < p[3]

    elif(p[2] == 'GR'):
        p[0] = p[1] > p[3]
    
    elif(p[2] == 'LEEQ'):
        p[0] = p[1] <= p[3]
    
    elif(p[2] == 'GREQ'):
        p[0] = p[1] >= p[3]


# Unary Expressions
def p_numeric_complement(p):
    '''numeric_complement : SUB arithmetic_expression'''
    p[0] = - p[2]

def p_boolean_complement(p):
    '''boolean_complement : COMPL boolean_expression'''
    p[0] = not (p[2])


# Functions
def p_justword_func(p):
    '''justword_func : JUSTWORD'''

    JustWord(input=None) #falta esta en ast


def p_length_func(p):
    '''length_func : LENGTH arithmetic_expression'''

    Length(input=None, length=p[2]) #falta esta en ast


def p_touppercase_func(p):
    '''touppercase_func : TOUPPERCASE
                        | TOUPPERCASE STRING'''

    if(len[p] == 2):
        ToUpperCase(input=None)
    else:
        ToUpperCase(input=p[1])


def p_slice_func(p):
    '''slice_func : SLICE arithmetic_expression
                  | SLICE STRING arithmetic_expression'''
    
    if(len[p] == 3):
        Slice(input=None, length=p[2])
    else:
        Slice(input=p[p[2]], length=p[3])
#--------------


def p_empty(p):
    '''empty : '''

def p_error(p):
    # print(f'Syntax error at {p.value!r}')
    print("Syntax error in input!")

parser = yacc(debug=yaccdebug)

#myLex = lexer.Lexer()
#lex = myLex.lexer
#file = open('test.txt')
#result = parser.parse('USE pdf "test";')
#file.close()
#print(result)