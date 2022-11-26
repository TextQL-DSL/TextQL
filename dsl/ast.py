from dsl_builtins.use import ReadPDF, ReadDocx

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
    def __init__(self, useStatement, statementList = []):
        super(Script, self).__init__()
        self.useStatement = useStatement
        self.statementList = statementList

class Statement(ASTNode):

    def __init__(self):
        super().__init__()

    def eval(self, globalDict):
        pass

class StatementList(ASTNode):
    
    def __init__(self, statementlist):
        super().__init__()
        self.statementList = statementlist


class Define(Statement):
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

    
    def eval(self, globalDict):
        globalDict[id] = self.expression.eval(globalDict)
        print(id, globalDict[id])

class Query(Statement):

    def __init__(self, functions):
        super(Query, self).__init__()
        self.functions = functions

    def eval(self, text, globalDict):
        for function in self.functions:
            text = function.eval(text, globalDict)
        
        return text



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

    def eval(self, globalDict):
        pass


class Number(Const):
    '''
    NUMBER -> number_value
    '''
    def __init__(self, value):
        super(Number, self).__init__()
        self.value = value

    def eval(self, globalDict):
        try:
            return float(self.value)
        except:
            assert f"{self.value} is not of type number."

class String(Const):
    '''
    STRING -> string_value
    '''
    def __init__(self, value):
        super(String, self).__init__()
        self.value = value[1:-1] # remove quotes

    def eval(self, globalDict):
        try:
            return str(self.value)
        except:
            assert f"{self.value} is not of type string."

class Boolean(Const):
    '''
    BOOLEAN ->  false
                | true
    '''
    def __init__(self, value):
        super(Boolean, self).__init__()
        self.value = value

    def eval(self, globalDict):
        try:
            return bool(self.value)
        except:
            assert f"{self.value} is not of type boolean."
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

    def eval(self, globalDict):
        pass




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
        
    def eval(self, globalDict):
        if id in globalDict.keys():
            return globalDict[id]
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

    def eval(self, globalDict):
        pass

#region Binary Boolean Operations
class Equal(BinaryExpression):
    def __init__(self, left, right):
        super(Equal, self).__init__()
        self.symbol = '=='
        self.left = left
        self.right = right

    def eval(self, globalDict):
        try:
            return self.left.eval() == self.right.eval()
        except:
            assert f"Invalid == operation exception."


class Grater(BinaryExpression):
    def __init__(self, left, right):
        super(Grater, self).__init__()
        self.symbol = '>'
        self.left = left
        self.right = right


    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) > self.right.eval(globalDict)
        except:
            assert f"Invalid > operation exception."


class Smaller(BinaryExpression):
    def __init__(self, left, right):
        super(Smaller, self).__init__()
        self.symbol = '<'
        self.left = left
        self.right = right

    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) < self.right.eval(globalDict)
        except:
            assert f"Invalid < operation exception."



class GraterEqual(BinaryExpression):
    def __init__(self, left, right):
        super(GraterEqual, self).__init__()
        self.symbol = '>='
        self.left = left
        self.right = right


    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) >= self.right.eval(globalDict)
        except:
            assert f"Invalid >= operation exception."



class SmallerEqual(BinaryExpression):
    def __init__(self, left, right):
        super(SmallerEqual, self).__init__()
        self.symbol = '<='
        self.left = left
        self.right = right

    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) <= self.right.eval(globalDict)
        except:
            assert f"Invalid <= operation exception."


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

    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) + self.right.eval(globalDict)
        except:
            assert f"Invalid + operation exception."


class Substraction(BinaryExpression):
    '''
    SUBSTRACTION -> EXPRESSION - EXPRESSION
    '''
    def __init__(self, left, right):
        super(Substraction, self).__init__()
        self.symbol = '-'
        self.left = left
        self.right = right

    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) - self.right.eval(globalDict)
        except:
            assert f"Invalid - operation exception."


class Product(BinaryExpression):
    '''
    PRODUCT -> EXPRESSION * EXPRESSION
    '''
    def __init__(self, left, right):
        super(Product, self).__init__()
        self.symbol = '*'
        self.left = left
        self.right = right


    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) * self.right.eval(globalDict)
        except:
            assert f"Invalid * operation exception."


class Division(BinaryExpression):
    '''
    DIVISION -> EXPRESSION / EXPRESSION
    '''
    def __init__(self, left, right):
        super(Division, self).__init__()
        self.symbol = '/'
        self.left = left
        self.right = right

    
    def eval(self, globalDict):
        try:
            return self.left.eval(globalDict) / self.right.eval(globalDict)
        except:
            assert f"Invalid / operation exception."


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


    def eval(self, globalDict):
        try:
            return self.thenExpression.eval(globalDict) if self.ifPredicate.eval(globalDict) else self.elseExpression.eval(globalDict)
        except:
            assert f"Invalid IF THEN ELSE operation exception."



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

    def eval(self, globalDict):
        globalText = ''
        if self.docExtension.doc_extension == 'doc':
            globalText = ReadDocx(self.path.value)
        elif self.docExtension.doc_extension == 'pdf':
            globalText = ReadPDF(self.path.value)
        else:
            assert f"Not supported extension {self.docExtension.doc_extension}."

        return globalText





class Function(ASTNode):
    def __init__(self):
        super(Function, self).__init__()


# Modify like functions.
class Modify(Function):
    def __init__(self):
        super(Modify, self).__init__()

    def eval(self, text, globalDict):
        return text


class ToUpperCase(Modify):
    def __init__(self):
        super(ToUpperCase, self).__init__()
        self.name = '_touppercase'

    def eval(self, text, globalDict):
        text = [str.upper(word) for word in text]
        return text


class Slice(Modify):
    def __init__(self, lengthExpression):
        super(Slice, self).__init__()
        self.name = '_slice'
        self.lengthExpression = lengthExpression

    def eval(self, text, globalDict):
        exprResult = self.lengthExpression.eval(globalDict)
        text = [word[:exprResult] for word in text]
        return text

# Filter like functions.
class Filter(Function):
    def __init__(self):
        super(Filter, self).__init__()

    def eval(self, text, globalDict):
        return text

class JustWord(Filter):
    def __init__(self):
        super(JustWord, self).__init__()
        self.name = 'JUSTWORD'

    def eval(self, text, globalDict):
        text = [word for word in text if str.isalpha(word)]
        return text

class Length(Filter):
    def __init__(self, lengthExpression):
        super(Length, self).__init__()
        self.lengthExpression = lengthExpression

    def eval(self, text, globalDict):
        exprResult = self.lengthExpression.eval(globalDict)
        text = [word for word in text if len(word) <= exprResult]
        return text

