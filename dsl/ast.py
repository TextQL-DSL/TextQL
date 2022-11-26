from dsl_builtins.use import ReadPDF, ReadDocx
from dsl_builtins.modification_functions import ModdificationFunctions
from dsl_builtins.filter_functions import filter_just_word, filter_length

globalList = []
globalDict = {}

class ASTNode:
    def __init__(self):
        self.line = 0
        self.pos = 0
    
    def cls(self):
        return str(self.__class__.__name__)

#region SCRIPT *******************

class Script(ASTNode):
    '''
    SCRIPT -> USE QUERY 
            | USE DEFINE
            | USE
    '''
    def __init__(self, useStatement, queries, defines):
        super(Script, self).__init__()
        self.useStatement = useStatement
        self.queries = queries
        self.defines = defines

class Query(ASTNode):

    def __init__(self, functions):
        super(Query, self).__init__()
        self.functions = functions



#endregion


#region CONSTANTS ******************
class Const(ASTNode):
    '''
    CONST -> NUMBER
            | STRING
            | BOOLEAN
    '''
    def __init__(self):
        super(Const, self).__init__()


class Number(Const):
    '''
    NUMBER -> number_value
    '''
    def __init__(self, value):
        super(Number, self).__init__()
        self.value = value


class String(Const):
    '''
    STRING -> string_value
    '''
    def __init__(self, value):
        super(String, self).__init__()
        self.value = value[1:-1] # remove quotes


class Boolean(Const):
    '''
    BOOLEAN ->  false
                | true
    '''
    def __init__(self, value):
        super(Boolean, self).__init__()
        self.value = value
#endregion



# Expressions.
class Expression(ASTNode):
    '''
    EXPRESION ->  UNARY_EXPRESSION
                | BINARY_EXPRESSION
                | DEFINE_EXPRESSION
                | IF_THEN_ELSE_EXPRESSION
                | e
    '''
    def __init__(self):
        super(Expression, self).__init__()

    def eval(self):
        pass


class Define(Expression):
    '''
    DEFINE ->   define type id = EXPRESSION;
    '''

    def __init__(self, type, id, expression):
        super(Define, self).__init__()
        self.type = type
        self.id = id
        self.expression = expression

        globalDict[id] = self
        print(id, ' = ', globalDict[id].expression)
        print('globalList = ', len(globalList))
        print('globalDict = ', len(globalDict))


class IdAccess(Expression):

    def __init__(self, id: str):
        super(IdAccess, self).__init__()
        self.value = None
        self.setValue(id)

    def setValue(self, id):
        id = id[1:]
        if id in globalDict.keys():
            self.value = globalDict[id]
        else:
            assert f"ID {id} is not defined." 
        

# Binary Expression *********************
class BinaryExpression(Expression):
    '''
    BINARY_EXPRESSION -> BINARY_ARITHMETIC_EXPRESSION
                        | BINARY_BOOLEAN_EXPRESSION
                        | BINARY_STRING_EXPRESSION
    '''
    def __init__(self):
        super(BinaryExpression, self).__init__()

#region Binary Boolean Operations
class Equal(BinaryExpression):
    def __init__(self, left, right):
        super(Equal, self).__init__()
        self.symbol = '=='
        self.left = left
        self.right = right


class Grater(BinaryExpression):
    def __init__(self, left, right):
        super(Grater, self).__init__()
        self.symbol = '>'
        self.left = left
        self.right = right


class Smaller(BinaryExpression):
    def __init__(self, left, right):
        super(Smaller, self).__init__()
        self.symbol = '<'
        self.left = left
        self.right = right


class GraterEqual(BinaryExpression):
    def __init__(self, left, right):
        super(GraterEqual, self).__init__()
        self.symbol = '>='
        self.left = left
        self.right = right


class SmallerEqual(BinaryExpression):
    def __init__(self, left, right):
        super(SmallerEqual, self).__init__()
        self.symbol = '<='
        self.left = left
        self.right = right


#endregion

#region Binary Arithmetic Operations
class Addition(BinaryExpression):
    '''
    ADITION -> EXPRESSION + EXPRESSION
    '''
    def __init__(self, left, right):
        super(Addition, self).__init__()
        self.symbol = '+'
        self.left = left
        self.right = right


class Substraction(BinaryExpression):
    '''
    SUBSTRACTION -> EXPRESSION - EXPRESSION
    '''
    def __init__(self, left, right):
        super(Substraction, self).__init__()
        self.symbol = '-'
        self.left = left
        self.right = right


class Product(BinaryExpression):
    '''
    PRODUCT -> EXPRESSION * EXPRESSION
    '''
    def __init__(self, left, right):
        super(Product, self).__init__()
        self.symbol = '*'
        self.left = left
        self.right = right


class Division(BinaryExpression):
    '''
    DIVISION -> EXPRESSION / EXPRESSION
    '''
    def __init__(self, left, right):
        super(Division, self).__init__()
        self.symbol = '/'
        self.left = left
        self.right = right

#endregion

#region Unary Operations
class UnaryExpression(Expression):
    def __init__(self):
        super().__init__()


class NumericComplement(UnaryExpression):
    def __init__(self, numericExpression):
        super(NumericComplement, self).__init__()
        self.symbol = '-'
        self.numericExpression = numericExpression


class BooleanComplement(UnaryExpression):
    def __init__(self, booleanExpression):
        super(BooleanComplement, self).__init__()
        self.symbol = '!'
        self.booleanExpression = booleanExpression

#endregion

class IfThenElseExpression(Expression):

    def __init__(self, ifPredicate, thenExpression, elseExpression):
        super(IfThenElseExpression, self).__init__()
        self.ifPredicate = ifPredicate
        self.thenExpression = thenExpression
        self.elseExpression = elseExpression



# Definition of a program.


class DocExtension(ASTNode):
    '''
    DOC_EXTENSION -> docx 
                    | pdf
    '''
    def __init__(self, doc_extension: str):
        super(DocExtension, self).__init__()
        self.doc_extension = doc_extension


class Use(ASTNode):
    '''
    USE -> use DOC_EXTENSION path ;
    '''
    def __init__(self, path, docExtension: DocExtension):
        super(Use, self).__init__()
        self.path = path
        self.docExtension = docExtension
        self.eval()

    def eval(self):
        if self.docExtension.doc_extension == 'doc':
            globalList = ReadDocx(self.path.value)
            print()
            print(globalList)
        elif self.docExtension.doc_extension == 'pdf':
            globalList = ReadPDF(self.path.value)
            print()
            print(globalList)
        else:
            assert f"Not supported extension {self.docExtension.doc_extension}."





class Function(ASTNode):
    def __init__(self):
        super(Function, self).__init__()


# Modify like functions.
class Modify(Function):
    def __init__(self):
        super(Modify, self).__init__()


class ToUpperCase(Modify):
    def __init__(self, input):
        super(ToUpperCase, self).__init__()
        self.name = '_touppercase'
        self.input = input

        if(self.input == None):
            self.input = globalList

        globalList = ModdificationFunctions.toUpperCase(self.input)


class Slice(Modify):
    def __init__(self, input, length):
        super(Slice, self).__init__()
        self.name = '_slice'
        self.input = input
        self.length = length

        if(self.input == None):
            self.input = globalList

        globalList = ModdificationFunctions.wordSlice(self.input, self.length)


# Filter like functions.
class Filter(Function):
    def __init__(self):
        super(Filter, self).__init__()


class JustWord(Filter):
    def __init__(self, input):
        super(JustWord, self).__init__()
        self.name = 'JUSTWORD'
        self.input = input

        if(self.input == None):
            self.input = globalList

        globalList = filter_just_word(self.input)


class Length(Filter):
    def __init__(self, input, length):
        super(Length, self).__init__()
        self.input = input
        self.length = length

        if(self.input == None):
            self.input = globalList

        globalList = filter_length(self.input, self.length)


