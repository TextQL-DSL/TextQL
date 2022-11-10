class TextQL_Tokens:
    
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