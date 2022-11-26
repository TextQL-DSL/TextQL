from ply.yacc import yacc, yaccdebug
from dsl.ast import *
from dsl.lexer import Lexer


PRSTX1 = "SyntacticError: ERROR at or near"
PREOF = "SyntacticError: ERROR at or near EOF"

lexer = Lexer()
lexer.build()
tokens = lexer.tokens
error_list = []


precedence = (
    ('right', 'ASSIGN'),
    ('nonassoc', 'EQ', 'LE', 'GR', 'LEEQ', 'GREQ'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV')
)

#--------------
def p_script(p):
    '''script : use SEMICOLON statement_list
              | use SEMICOLON'''

    script = Script(p[1], None)
    if(len(p) == 4):
        script.statementList = p[3]
        
    p[0] = script


def p_use(p):
    '''use : USE PDF STRING
           | USE DOC STRING'''
    doc_ext = DocExtension(p[2])
    path = String(p[3])
    use = Use(path, doc_ext)
    p[0] = use
    # use.eval()

    if(len(p) == 6):
        p[0] = p[5]

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | statement'''
    
    
    if len(p) == 2 and p[1]:
        p[0] = []
        p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[2]
        if not p[0]:
            p[0] = []
        if p[2]:
            p[0] = [p[1]] + p[2]
    
    # if(len(p) == 2):
    #     p[0] = p[1]
    
    # else:
    #     p[0] = (p[1], p[3])



def p_statement(p):
    '''statement : query SEMICOLON 
                 | define SEMICOLON'''
    
    p[0] = p[1]
    # if(len(p) == 2):
    #     p[0] = p[1]
    
    # else:
    #     p[0] = (p[1], p[3])


def p_define(p):
    '''define : DEFINE TYPE_STRING ID ASSIGN expression
              | DEFINE TYPE_BOOLEAN ID ASSIGN expression
              | DEFINE TYPE_NUMBER ID ASSIGN expression'''
    
    p[0] = Define(p[2], p[3], p[5])


def p_query(p):
    '''query : QUERY function_list'''
    query = Query(p[2])
    p[0] = query

def p_function_list(p):
    '''function_list : function function_list
                     | function'''
    if len(p) == 2 and p[1]:
        p[0] = []
        p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[2]
        if not p[0]:
            p[0] = []
        if p[1]:
            p[0] = [p[1]] + p[2]

def p_function(p):
    '''function : justword_func
                | length_func
                | touppercase_func
                | slice_func'''
    
    p[0] = p[1]

# Binary Expressions

def p_arithmetic_expression_number(p):
    '''expression : NUMBER'''
    p[0] = Number(p[1])


def p_binary_expression(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MULT expression
                  | expression DIV expression
                  | expression EQ expression
                  | expression LE expression
                  | expression GR expression
                  | expression LEEQ expression
                  | expression GREQ expression'''

    if(p[2] == '+'):
        p[0] = Addition(p[1], p[3])

    elif(p[2] == '-'):
        p[0] = Substraction(p[1], p[3])

    elif(p[2] == '*'):
        p[0] = Product(p[1], p[3])
    
    elif(p[2] == '/'):
        p[0] = Division(p[1],  p[3])

    elif(p[2] == '=='):
        p[0] = Equal(p[1], p[3])

    elif(p[2] == '<'):
        p[0] = Smaller(p[1], p[3])

    elif(p[2] == '>'):
        p[0] = Grater(p[1], p[3])
    
    elif(p[2] == '<='):
        p[0] = SmallerEqual(p[1], p[3])
    
    elif(p[2] == '>='):
        p[0] = GraterEqual(p[1], p[3])


def p_parenthized_expression(p):
    '''expression : 
                  | LPARENT expression RPARENT'''
    p[0] = p[2]


def p_boolean_expression_boolean(p):
    '''expression : BOOLEAN'''

    p[0] = Boolean(True if p[1] == 'true' else False)


# def p_boolean_expression(p):
#     '''expression : expression EQ expression
#                   | expression LE expression
#                   | expression GR expression
#                   | expression LEEQ expression
#                   | expression GREQ expression'''
    
#     if(len(p) == 2):
#         p[0] = p[1]
    
#     elif(p[2] == '=='):
#         p[0] = Equal(p[1], p[3])

#     elif(p[2] == '<'):
#         p[0] = Smaller(p[1], p[3])

#     elif(p[2] == '>'):
#         p[0] = Grater(p[1], p[3])
    
#     elif(p[2] == '<='):
#         p[0] = SmallerEqual(p[1], p[3])
    
#     elif(p[2] == '>='):
#         p[0] = GraterEqual(p[1], p[3])


def p_string(p):
    '''expression : STRING'''
    p[0] = String(p[1])


def p_id_access(p):
    '''expression : ID_ACCESS'''
    p[0] = IdAccess(p[1])


def p_ite(p):
    '''expression : IF expression THEN expression ELSE expression'''
    p[0] = IfThenElseExpression(p[2], p[4], p[6])

# Unary Expressions
def p_numeric_complement(p):
    '''numeric_complement : SUB expression'''
    p[0] = - p[2]

def p_boolean_complement(p):
    '''expression : COMPL expression'''
    p[0] = not (p[2])


# Functions
def p_justword_func(p):
    '''justword_func : JUSTWORD'''

    p[0] = JustWord()


def p_length_func(p):
    '''length_func : LENGTH expression'''

    p[0] = Length(p[2])


def p_touppercase_func(p):
    '''touppercase_func : TOUPPERCASE'''
    p[0] = ToUpperCase()


def p_slice_func(p):
    '''slice_func : SLICE expression'''
    p[0] = Slice(p[2])
#--------------


def p_empty(p):
    '''empty : '''
    p[0] = None

# def p_error(p):
#     # print(f'Syntax error at {p.value!r}')
#     print("Syntax error in input!")

def p_error(p):
    """
    Error rule for Syntax Errors handling and reporting.
    """
    if p is None:
        print(f'(0,0) - {PREOF}')
    else:
        print(f'({p.lineno}, {p.lexpos}) - {PRSTX1} "{p.value}"')
        parser.errok()


parser = yacc(debug=yaccdebug)

#myLex = lexer.Lexer()
#lex = myLex.lexer
#file = open('test.txt')
#result = parser.parse('USE pdf "test";')
#file.close()
#print(result)