from dsl.lexer import lexer
from ply import yacc

tokens = lexer.tokens

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV')
)

def handler():
    pass
handler = handler()


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
    '''USE : extension path'''
    p[0] = ('use', p[2], p[1])
    pass

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


parser = yacc.yacc()

def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p
