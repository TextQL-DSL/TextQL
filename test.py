from dsl.parser import parser
from dsl.lexer import Lexer

#data = "USE doc '/home/rp/Documents/repos/TextQL/data.docx';"
data = "USE pdf '/home/rp/Documents/repos/TextQL/data.pdf';"

lexer = Lexer()
lexer.build()
lexer.test(data)

print(parser.parse(data))