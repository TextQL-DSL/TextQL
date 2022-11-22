# from ast import keyword
# from tokens import TextQL_Tokens
import ply.lex as lex

keywords = {
    "JUSTWORD": "JUSTWORD",
    "LENGTH": "LENGTH",
    "_touppercase": "TOUPPERCASE",
    "_slice": "SLICE",
    "IF": "IF",
    "THEN": "THEN",
    "ELSE": "ELSE",
    "define": "DEFINE",
    "USE": "USE"
}

tokens = [
    'ID', 'LPARENT', 'RPARENT', 'SEMICOLON', 'ADD', 'SUB', 'ASSIGN', 'COMPL',
    'DIV', 'MULT', 'EQ', 'LE', 'GR', 'LEEQ', 'GREQ', 'NUMBER', 'BOOLEAN', 'STRING'
] + list(keywords.values())

ignored = [' ', '\f', '\r', '\t', '\v']

t_LPARENT = r'\('   # (
t_RPARENT = r'\)'   # )
t_SEMICOLON = r'\;'  # ;
t_ADD = r'\+'       # +
t_SUB = r'\-'       # -
t_DIV = r'\/'       # /
t_MULT = r'\*'      # *
t_EQ = r'\=\='      # ==
t_LE = r'\<'        # <
t_GR = r'\>'        # >
t_LEEQ = r'\<\='    # <=
t_GREQ = r'\>\='    # >=
t_ASSIGN = r'\='    # =
t_COMPL = r'\!'     # !

def t_KEY(t):
    r'[_|A-Z][A-Za-z_]*|define'
    t.type = keywords.get(t.value)
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    t.type = "BOOLEAN"
    return t

def t_ID(t):
    r'[a-z][A-Za-z0-9_]*'
    t.type = "ID"
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    t.type = "NUMBER"
    return t


# def t_TYPE(t):
#     r'[a-zA-Z][a-zA-Z_0-9]'
#     t.type = keywords.get(t.value, "TYPE")
#     return t


def t_STRING(t):
    r'"[^\0\n"]*(\\\n[^\0\n"]*)*"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '{}'".format(t.value[0]))
    t.lexer.skip(1)

t_ignore = ''.join(ignored)

def find_column(input, token):
    if token:
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1


lexer = lex.lex()
data = "define \"hola\" _slice THEN perro true"
lexer.input(data)
while True:
    tok = lexer.token()
    col = find_column(data, tok)
    if tok is None:
        break
    print(tok.value,tok.type,tok.lineno,col)