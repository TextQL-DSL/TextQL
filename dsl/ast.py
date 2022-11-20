from ..Builtins.use import *

globalList = []

class ASTNode:
    def __init__(self):
        self.line = 0
        self.pos = 0


# Expressions.
class Expression(ASTNode):
    '''
    EXPRESION -> CONST
                | DEFINE
                | UNARY_EXPRESSION
                | BINARY_EXPRESSION
                | e
    '''
    def __init__(self):
        super(Expression, self).__init__()

    def eval(self):
        pass



# Constants and variables.
class Variable(ASTNode):
    '''
    VARIABLE -> id
    '''
    def __init__(self, name):
        super(Variable, self).__init__()
        self.name = name


class Const(Expression):
    '''
    CONST -> NUMBER
            | STRING
            | BOOLEAN
    '''
    def __init__(self, value):
        super(Const, self).__init__()
        self.value = value


class Number(Const):
    '''
    NUMBER -> number_value
    '''
    def __init__(self):
        super(Number, self).__init__()


class String(Const):
    '''
    STRING -> string_value
    '''
    def __init__(self):
        super(String, self).__init__()


class Boolean(Const):
    '''
    BOOLEAN ->  false
                | true
    '''
    def __init__(self):
        super(Boolean, self).__init__()


class Define(Expression):
    '''
    DEFINE ->   define STRING_DEFINE ;
                | define NUMBER_DEFINE ;
                | define BOOLEAN_DEFINE ;
    '''

    def __init__(self):
        super().__init__()


class StringDefine(Define):
    '''
    STRING_DEFINE -> string VARIABLE = EXPRESSION
    '''
    def __init__(self, value: str, expression: Expression):
        super(StringDefine, self).__init__()
        self.value = value


class NumberDefine(Define):
    '''
    NUMBER_DEFINE -> number VARIABLE = EXPRESSION
    '''
    def __init__(self, value: float, expression: Expression):
        super(NumberDefine, self).__init__()
        self.value = value



class BooleanDefine(Define):
    '''
    NUMBER_DEFINE -> boolean VARIABLE = EXPRESSION
    '''
    def __init__(self, value: Boolean, expression: Expression):
        super(BooleanDefine, self).__init__()
        self.value = value


class StringDefine(Define):
    '''
    STRING_DEFINE -> string VARIABLE equal EXPRESSION
    '''
    def __init__(self, value: str, expression: Expression):
        super(StringDefine, self).__init__()
        self.value = value


#Binary Expression
class BinaryExpression(Expression):
    '''
    BINARY_EXPRESSION -> BINARY_ARITHMETIC_EXPRESSION
                        | BINARY_BOOLEAN_EXPRESSION
                        | BINARY_STRING_EXPRESSION
    '''
    def __init__(self, left, right):
        super(BinaryExpression, self).__init__()
        self.left = left
        self.right = right


# Arithmetic Expressions.
class BinaryArithmeticExpression(BinaryExpression):
    '''
    ARITHMETIC_EXPRESSION -> ADITION
                            | SUBSTRACTION
                            | PRODUCT
                            | DIVISION
    '''
    def __init__(self, left, right):
        super(BinaryArithmeticExpression, self).__init__(left, right)


class Addition(BinaryArithmeticExpression):
    '''
    ADITION -> EXPRESION + EXPRESION
    '''
    def __init__(self):
        super(Addition, self).__init__()


class Substraction(BinaryArithmeticExpression):
    '''
    SUBSTRACTION -> EXPRESSION - EXPRESSION
    '''
    def __init__(self):
        super(Substraction, self).__init__()


class Product(BinaryArithmeticExpression):
    '''
    PRODUCT -> EXPRESSION * EXPRESSION
    '''
    def __init__(self):
        super(Substraction, self).__init__()


class Division(BinaryExpression):
    '''
    DIVISION -> EXPRESSION / EXPRESSION
    '''
    def __init__(self):
        super(Division, self).__init__()


# Boolean Expressions.
class BinaryBooleanExpression(BinaryExpression):

    def __init__(self, left: Boolean, right: Boolean):
        super().__init__(left, right)
        


class Equal(BinaryExpression):
    def __init__(self):
        super(Equal, self).__init__()


class Grater(BinaryExpression):
    def __init__(self):
        super(Grater, self).__init__()


class Smaller(BinaryExpression):
    def __init__(self):
        super(Smaller, self).__init__()


class GraterEqual(BinaryExpression):
    def __init__(self):
        super(GraterEqual, self).__init__()


class SmallerEqual(BinaryExpression):
    def __init__(self):
        super(SmallerEqual, self).__init__()


class UnaryExpression(Expression):
    def __init__(self, right):
        super().__init__()
        self.right = right


class NumericComplement(UnaryExpression):
    def __init__(self):
        super(NumericComplement, self).__init__()


class BooleanComplement(UnaryExpression):
    def __init__(self):
        super(BooleanComplement, self).__init__()


class IfThenElseExpression(Expression):
    def __init__(self, ifPredicate, thenExpression, elseExpression):
        super(IfThenElseExpression, self).__init__()
        self.ifPredicate = ifPredicate
        self.thenExpression = thenExpression
        self.elseExpression = elseExpression



# Definition of a program.
class Script(ASTNode):
    '''
    SCRIPT -> USE STATEMENT 
            | USE
    '''
    def __init__(self, functList):
        super(Script, self).__init__()
        self.functList = functList


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

    def eval(self):
        if self.docExtension.doc_extension == 'docx':
            globalList = ReadDocx(self.path)
        elif self.docExtension.doc_extension == 'pdf':
            globalList = ReadPDF(self.path)
        else:
            assert f"Not supported extension {self.docExtension.doc_extension}."



class Statement(ASTNode):
    '''
    STATEMENT -> FUNCTION STATEMENT
                | DEFINE STATEMENT
                | e
    '''
    def __init__(self):
        super(Statement, self).__init__()


class Define(Statement):
    '''
    DEFINE -> define TYPE id = EXPRESSION;
    '''

    def __init__(self):
        super(Define, self).__init__()


class Function(ASTNode):
    def __init__(self, input):
        super(Function, self).__init__()
        self.input = input


# Modify like functions.
class Modify(Function):
    def __init__(self):
        super(Modify, self).__init__()


class ToUpperCase(Modify):
    def __init__(self):
        super(ToUpperCase, self).__init__()


class Slice(Modify):
    def __init__(self, take):
        super(Slice, self).__init__()
        self.take = take


# Filter like functions.
class Filter(Function):
    def __init__(self):
        super(Filter, self).__init__()


class JustWord(Filter):
    def __init__(self):
        super(JustWord, self).__init__()


class Length(Filter):
    def __init__(self, rightExpr):
        super(Length, self).__init__()
        self.rightExpr = rightExpr


