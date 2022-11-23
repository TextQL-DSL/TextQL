from dsl.lexer import lexer
from ply.yacc import yacc

tokens = lexer.tokens

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV')
)

#--------------
def p_script(p):
    '''script : USE statement
              | USE'''
    pass

# esto es ambiguo, el primer statement se cambia por lo que hereda de statement
def p_statement(p):
    '''statement : statement FUNC
                 | statement DEF
                 | statement'''
    pass

def p_use(p):
    '''command : USE STRING'''
    p[0] = ('USE', p[2])

#Binary Expressions
def p_arithmetic_expression(p):
    '''expr : expr ADD expr
            | expr SUB expr
            | expr MULT expr
            | expr DIV expr'''    
    p[0] = ('arithmetic_expression', p[2], p[1], p[3])

def p_boolean_expression(p):
    '''expr : expr EQ expr ==
               | expr LE expr <
               | expr GR expr >
               | expr LEEQ expr <=
               | expr GREQ expr >='''
    p[0] = ('boolean_expression', p[2], p[1], p[3])

#Unary Expressions
def p_numeric_complement(p):
    '''expr : - expr'''
    p[0] = ('numeric_complement', '-', p[2])

def p_boolean_complement(p):
    '''expr : ! expr'''
    p[0] = ('boolean_complement', '!', p[2])

def p_const(p):
    '''expr : const'''
    p[0] = ('const', p[1])

def p_variable(p):
    '''expr : variable'''
    p[0] = ('variable', p[1])

#--------------
def p_function_modify(p):
    pass

def p_function_filter(p):
    pass

#If Then Else
def p_ite(p):
    pass

def p_empty(p):
    '''empty : '''

def p_error(p):
    # print(f'Syntax error at {p.value!r}')
    print("Syntax error in input!")

parser = yacc()