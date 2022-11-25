from ply.yacc import yacc
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
    use = Use(path, doc_ext)
    use.eval()

    if(len(p) == 6):
        p[0] = p[5]


def p_statement(p):
    '''statement : query SEMICOLON statement 
                 | define SEMICOLON statement
                 | empty'''
    pass


def p_define(p):
    '''define : DEFINE TYPE_STRING ID ASSIGN STRING
              | DEFINE TYPE_BOOLEAN ID ASSIGN boolean_expression
              | DEFINE TYPE_NUMBER ID ASSIGN arithmetic_expression'''


def p_query(p):
    '''query : QUERY function'''


def p_function(p):
    '''function : justword_func function
                | length_func function
                | touppercase_func function
                | slice_func function
                | empty'''


# def p_expr(p):
#     '''expr : arithmetic_expression
#             | boolean_expression
#             | ite'''

#Binary Expressions
def p_arithmetic_expression(p):
    '''arithmetic_expression : arithmetic_expression ADD arithmetic_expression
                             | arithmetic_expression SUB arithmetic_expression
                             | arithmetic_expression MULT arithmetic_expression
                             | arithmetic_expression DIV arithmetic_expression
                             | numeric_complement
                             | NUMBER'''    
    p[0] = ('arithmetic_expression', p[2], p[1], p[3])

def p_boolean_expression(p):
    '''boolean_expression : boolean_expression EQ boolean_expression
                          | boolean_expression LE boolean_expression
                          | boolean_expression GR boolean_expression
                          | boolean_expression LEEQ boolean_expression
                          | boolean_expression GREQ boolean_expression
                          | boolean_complement
                          | BOOLEAN'''
    p[0] = ('boolean_expression', p[2], p[1], p[3])

#Unary Expressions
def p_numeric_complement(p):
    '''numeric_complement : SUB arithmetic_expression'''
    p[0] = ('numeric_complement', '-', p[2])

def p_boolean_complement(p):
    '''boolean_complement : COMPL boolean_expression'''
    p[0] = ('boolean_complement', '!', p[2])

# def p_const(p):
#     '''expr : const'''
#     p[0] = ('const', p[1])

# def p_variable(p):
#     '''expr : variable'''
#     p[0] = ('variable', p[1])

#----------------functions
def p_justword_func(p):
    '''justword_func : JUSTWORD'''


def p_length_func(p):
    '''length_func : LENGTH arithmetic_expression'''


def p_touppercase_func(p):
    '''touppercase_func : TOUPPERCASE'''


def p_slice_func(p):
    '''slice_func : SLICE arithmetic_expression'''
#--------------
# def p_function_modify(p):
#     pass

# def p_function_filter(p):
#     pass

#If Then Else
# def p_ite(p):
#     '''ite : IF boolean_expression THEN arithmetic_expression ELSE arithmetic_expression'''
#     pass

def p_empty(p):
    '''empty : '''

def p_error(p):
    # print(f'Syntax error at {p.value!r}')
    print("Syntax error in input!")

parser = yacc()



# myLex = lexer.Lexer()
# lex = myLex.lexer

#file = open('test.txt')
#result = parser.parse('USE pdf "test";')
#file.close()
#print(result)