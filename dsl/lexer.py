class Lexer:

    @property
    def basic_tokens(self):
        return ["ID", "TYPE", "LPARENT", "RPARENT", "SEMICOLON", "ADD", "SUB", "ASSIGN", "COMPL"
            "DIV", "MULT", "EQ", "LE", "GR", "LEEQ", "GREQ", "NUMBER", "BOOLEAN", "STRING"]

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
            "USE": "USE"
        }


    def __init__(self) -> None:
        self.tokens = self.basic_tokens + list(self.keyword_tokens.values())


    t_LPARENT = r'\('
    t_RPARENT = r'\)'
    t_SEMICOLON = r'\;'
    t_ADD = r'\+'
    t_SUB = r'\-'
    t_DIV = r'\/'
    t_MULT = r'\*'
    t_EQ = r'\=\='
    t_LE = r'\<'
    t_GR = r'\>'
    t_LEEQ = r'\<\='
    t_GREQ = r'\>\='
    t_ASSIGN = r'\='
    t_COMPL = r'\!'

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

    

    



if __name__ == "__main__":
    lexer = Lexer()
    print(lexer.tokens)