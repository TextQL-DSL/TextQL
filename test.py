from dsl.parser import parser
from dsl.lexer import Lexer
from dsl.ast import *
from dsl.interpreter import TextQLInterpreter

#data = "USE doc '/home/rp/Documents/repos/TextQL/data.docx';"
#data = "USE pdf '/home/rp/Documents/repos/TextQL/data.pdf';"

lexer = Lexer()
lexer.build()

file = open('./test.txt')
data = file.read()
file.close

# print()
# print()
# print(data)
# print()
# print()

# lexer.test(data)
# print()
# print()

ast = parser.parse(data)

print()
print()
for statement in ast.statementList:
    print(statement)


interpreter = TextQLInterpreter(ast)
interpreter.run()