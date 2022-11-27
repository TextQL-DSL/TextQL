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
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'), 
)

#--------------
def p_script(p):
    '''script : use SEMICOLON statement_list
              | use SEMICOLON'''

    script = Script(p[1], None)
    if(len(p) == 4):
        script.statementList = p[3]
    else:
        script.statementList = []
        
    p[0] = script


def p_use(p):
    '''use : USE PDF STRING
           | USE DOC STRING'''
    doc_ext = DocExtension(p[2])
    path = String(p[3])
    use = Use(path, doc_ext)
    use.line = p.lineno(1)
    use.pos = p.lexpos(1)
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
    define = Define(p[2], p[3], p[5])
    define.line = p.lineno(1)
    define.pos = p.lexpos(1)
    p[0] = define


def p_query(p):
    '''query : QUERY function_list'''
    query = Query(p[2])
    query.line = p.lineno(1)
    query.pos = p.lexpos(1)
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
                | slice_func
                | ite_function'''
    
    p[0] = p[1]

# Binary Expressions

def p_arithmetic_expression_number(p):
    '''expression : NUMBER'''
    number = Number(p[1])
    number.line = p.lineno(1)
    number.pos = p.lexpos(1)
    p[0] = number


def p_number_compl(p):
    '''expression : SUB expression %prec UMINUS'''
    compl = ArtithmeticComplement(p[2])
    compl.line = p.lineno(1)
    compl.pos = p.lexpos(1)
    p[0] = compl


# def p_boolean_complement

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
        add = Addition(p[1], p[3])
        add.line = p.lineno(1)
        add.pos = p.lexpos(1)
        p[0] = add

    elif(p[2] == '-'):
        sub = Substraction(p[1], p[3])
        sub.line = p.lineno(1)
        sub.pos = p.lexpos(1)
        p[0] = sub

    elif(p[2] == '*'):
        prod = Product(p[1], p[3])
        prod.line = p.lineno(1)
        prod.pos = p.lexpos(1)
        p[0] = prod
    
    elif(p[2] == '/'):
        div = Division(p[1],  p[3])
        div.line = p.lineno(1)
        div.pos = p.lexpos(1)
        p[0] = div

    elif(p[2] == '=='):
        eq = Equal(p[1], p[3])
        eq.line = p.lineno(1)
        eq.pos = p.lexpos(1)
        p[0] = eq

    elif(p[2] == '<'):
        sm = Smaller(p[1], p[3])
        sm.line = p.lineno(1)
        sm.pos = p.lexpos(1)
        p[0] = sm

    elif(p[2] == '>'):
        gr = Grater(p[1], p[3])
        gr.line = p.lineno(1)
        gr.pos = p.lexpos(1)
        p[0] = gr
    
    elif(p[2] == '<='):
        smeq = SmallerEqual(p[1], p[3])
        smeq.line = p.lineno(1)
        smeq.pos = p.lexpos(1)
        p[0] = smeq
    
    elif(p[2] == '>='):
        greq = GraterEqual(p[1], p[3])
        greq.line = p.lineno(1)
        greq.pos = p.lexpos(1)
        p[0] = greq


def p_parenthized_expression(p):
    '''expression : 
                  | LPARENT expression RPARENT'''
    p[0] = p[2]


def p_boolean_expression_boolean(p):
    '''expression : BOOLEAN'''

    boolean = Boolean(True if p[1] == 'true' else False)
    boolean.line = p.lineno(1)
    boolean.pos = p.lexpos(1)
    p[0] = boolean

def p_string(p):
    '''expression : STRING'''
    string = String(p[1])
    string.line = p.lineno(1)
    string.pos = p.lexpos(1)
    p[0] = string


def p_id_access(p):
    '''expression : ID_ACCESS'''
    id = IdAccess(p[1])
    id.line = p.lineno(1)
    id.pos = p.lexpos(1)
    p[0] = id


def p_ite(p):
    '''expression : IF expression THEN expression ELSE expression'''
    ite = IfThenElseExpression(p[2], p[4], p[6])
    ite.line = p.lineno(1)
    ite.pos = p.lexpos(1)
    p[0] = ite

def p_boolean_complement(p):
    '''expression : COMPL expression'''
    boolCompl = BooleanComplement(p[2])
    boolCompl.line = p.lineno(1)
    boolCompl.pos = p.lexpos(1)
    p[0] = boolCompl


# Functions
def p_justword_func(p):
    '''justword_func : JUSTWORD'''
    justWord = JustWord()
    justWord.line = p.lineno(1)
    justWord.pos = p.lexpos(1)
    p[0] = justWord


def p_length_func(p):
    '''length_func : LENGTH expression'''
    length = Length(p[2])
    length.line = p.lineno(1)
    length.pos = p.lexpos(1)
    p[0] = length 


def p_touppercase_func(p):
    '''touppercase_func : TOUPPERCASE'''
    toUpper = ToUpperCase()
    toUpper.line = p.lineno(1)
    toUpper.pos = p.lexpos(1)
    p[0] = toUpper


def p_slice_func(p):
    '''slice_func : SLICE expression'''
    slice = Slice(p[2])
    slice.line = p.lineno(1)
    slice.pos = p.lexpos(1)
    p[0] = slice


def p_ite_function(p):
    '''ite_function : IF expression THEN function_list ELSE function_list'''
    iteF = IfThenElseFunction(p[2], p[4], p[6])
    iteF.line = p.lineno(1)
    iteF.pos = p.lexpos(1)
    p[0] = iteF
#--------------


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