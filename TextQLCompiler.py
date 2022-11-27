import sys
from dsl.parser import parser
from dsl.lexer import Lexer
from dsl.ast import *
from dsl.interpreter import TextQLInterpreter

#data = "USE doc '/home/rp/Documents/repos/TextQL/data.docx';"
#data = "USE pdf '/home/rp/Documents/repos/TextQL/data.pdf';"
def test():
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

    lexer.test(data)
    print()
    print()

    ast = parser.parse(data)

    print()
    print()
    for statement in ast.statementList:
        print(statement)


    interpreter = TextQLInterpreter(ast)
    interpreter.run()



test()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('How to run a TextQL program: python TextQLCompiler.py <file_path>')
        exit(1)
    filePath = sys.argv[2]

    data = ''
    try:
        file = open(filePath)
        data = file.read()
        file.close
    except:
        sys.stdout.write(f'Error opening file {filePath}.')
        exit(1)
            
    lexer = Lexer()
    lexer.build()
    ast = parser.parse(data)
    interpreter = TextQLInterpreter(ast)
    interpreter.run()
