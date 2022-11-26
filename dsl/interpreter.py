from dsl.ast import *

class TextQLInterpreter:

    def __init__(self, program) -> None:
        self.program = program

        print(program)

    
    def run(self):
        print('**********RUN**********')
        self.globalDict = {}            # All variables
        self.errors = []              # Indicates program error
        self.statements = self.program.statementList
        print(self.program)
        print(self.program.statementList)
        self.use = self.program.useStatement
        self.text = self.use.eval(self.globalDict)
        print('text\n', self.text)

        for line in self.statements:
            print(line)
            print(line.cls())
            cls = line.cls()

            if cls == 'Define':
                print('executing define')
                line.eval(self.globalDict)
            elif cls == 'Query':
                print('executing query')
                print(line.functions)
                self.text = line.eval(self.text, self.globalDict)


        print(self.text)