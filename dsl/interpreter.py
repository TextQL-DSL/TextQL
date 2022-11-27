import sys
from dsl.ast import *

class TextQLInterpreter:

    def __init__(self, program) -> None:
        self.program = program

    
    def run(self):
        
        self.globalDict = {}            # All variables
        self.errors:list[DSLError] = []              # Indicates program error
        self.statements = self.program.statementList
        self.use = self.program.useStatement
        self.text = self.use.eval(self.globalDict, self.errors)

        for line in self.statements:            
            cls = line.cls()

            if cls == 'Define':
                line.eval(self.globalDict, self.errors)
            elif cls == 'Query':
                self.text = line.eval(self.text, self.globalDict, self.errors)

        if len(self.errors) > 0:
            errorSet = list(set([(err.line,str(err)) for err in self.errors]))
            errorSet.sort(key=lambda x: x[0])
            errorSet = [err[1] for err in errorSet]
            for err in errorSet:
                sys.stderr.write(f'{str(err)}\n')
            exit(1)
        else:
            sys.stdout.write(f'{self.text}\n')