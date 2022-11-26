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

        for line in self.statements:
            print(line)
            # line.eval(self.globalDict)
            print(line.cls())

        for value in self.globalDict.values():
            print(value)