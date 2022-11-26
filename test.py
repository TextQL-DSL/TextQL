from dsl.parser import parser
from dsl.lexer import Lexer

#data = "USE doc '/home/rp/Documents/repos/TextQL/data.docx';"
#data = "USE pdf '/home/rp/Documents/repos/TextQL/data.pdf';"

lexer = Lexer()
lexer.build()

file = open('./test.txt')
data = file.read()
file.close

print()
print()
print(data)
print()
print()

lexer.test(data)
print()
print()
parser.parse(data)