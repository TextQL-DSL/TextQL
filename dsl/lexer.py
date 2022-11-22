from dsl.tokens import TextQL_Tokens
from ply.lex import lex


class Lexer:

    def __init__(self) -> None:
        self.t = TextQL_Tokens()
        self.tokens = self.t.tokens
        self.lastPosition = [-1]
        self.lexer = lex.lex(module=self)

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

    def t_BOOLEAN(self, t):
        r'(true|false)'
        t.value = True if t.value == "true" else False
        t.type = "BOOLEAN"
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        t.type = "NUMBER"
        return t

    def t_TYPE(self, t):
        r'[a-zA-Z][a-zA-Z_0-9]'
        t.type = self.keyword_tokens.get(t.value, "TYPE")
        return t

    def t_ID(self, t):
        r'\@[a-zA-Z][a-zA-Z_0-9]'
        t.type = "ID"
        return t

    def t_newline(self, t):
        r'\n'
        t.lexer.lineno += 1
        self.linelastpos.append(t.lexpos)

    # STRING
    def t_begin_STRING(self, t):
        r'"'
        t.lexer.begin("STRING")
        t.lexer.string_backslashed = False
        t.lexer.stringbuf = ""

    def t_STRING_end(self, t):
        r'"'
        if not t.lexer.string_backslashed:
            t.lexer.begin("INITIAL")
            t.value = t.lexer.stringbuf
            t.type = "STRING"
            return t
        else:
            t.lexer.stringbuf += '"'
            t.lexer.string_backslashed = False

    def t_STRING_anything(self, t):
        r'[^\n\x00]'
        if t.lexer.string_backslashed:
            if t.value in ['b', 't', 'n', 'f', '\\']:
                t.lexer.stringbuf += '\\'
            t.lexer.stringbuf += t.value
            t.lexer.string_backslashed = False
        else:
            if t.value != '\\':
                t.lexer.stringbuf += t.value
            else:
                t.lexer.string_backslashed = True

    t_STRING_ignore = ''

# Build the lexer object
lexer = lex()