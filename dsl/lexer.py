import ply.lex as lex


class Lexer:

    @property
    def basic_tokens(self):
        return ["ID", "TYPE", "LPARENT", "RPARENT", "SEMICOLON", "ADD", "SUB", "ASSIGN", "COMPL",
            "DIV", "MULT", "EQ", "LE", "GR", "LEEQ", "GREQ", "NUMBER", "BOOLEAN","STRING", "ID_ACCESS",
            "COMMENT"]


    @property
    def keyword_tokens(self) -> dict:
        return {
            "JUSTWORD": "JUSTWORD",
            "LENGTH": "LENGTH",
            "_touppercase": "TOUPPERCASE",
            "_slice": "SLICE",
            "IF": "IF",
            "THEN": "THEN",
            "ELSE": "ELSE",
            "define": "DEFINE",
            "USE": "USE",
            "pdf": "PDF",
            "doc": "DOC",
            "string": "TYPE_STRING",
            "boolean": "TYPE_BOOLEAN",
            "number": "TYPE_NUMBER",
            "QUERY": "QUERY"
        }

    def __init__(self,) -> None:
        self.tokens = self.basic_tokens + list(self.keyword_tokens.values())
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

    t_STRING = r'\'.*?\''
    # Ignored characters
    t_ignore = ' \t'


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

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if t.value in self.keyword_tokens.keys():
            t.type = self.keyword_tokens[t.value]
        else:
            t.type = "ID"
        
        return t

    def t_ID_ACCESS(self, t):
        r'@[a-zA-Z][a-zA-Z_0-9]*'
        t.type = "ID_ACCESS"
        
        return t

    def t_COMMENT(self, t):
        r'//.*'
        pass

    # Ignored token with an action associated with it
    def t_ignore_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')

    # Error handler for illegal characters
    def t_error(self, t):
        # print(f'Illegal character {t.value[0]!r}')
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

     # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break      # No more input
            print(tok)


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    _input = ""
    with open("test.txt") as file:
        _input = file.read()
    lexer.test(_input)