class ASTNode:

    def __init__(self):
        self.line = 0
        self.pos = 0


class Script(ASTNode):

    def __init__(self, functList):
        super(Script, self).__init__()
        self.functList = functList


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


# Constants and variables.

class Const(ASTNode):

    def __init__(self, value):
        super(Const, self).__init__()
        self.value = value


class Number(Const):
    
    def __init__(self):
        super(Number, self).__init__()


class String(Const):

    def __init__(self):
        super(String, self).__init__()


class Boolean(Const):

    def __init__(self):
        super(Boolean, self).__init__()


class Variable(ASTNode):

    def __init__(self, name):
        super(Variable, self).__init__()
        self.name = name


# Expssions.

class Expression(ASTNode):

    def __init__(self):
        super().__init__()


class BinaryExpression(Expression):

    def __init__(self, left, right):
        super(BinaryExpression, self).__init__()
        self.left = left
        self.right = right

# Arithmetic Expressions.
class Adition(BinaryExpression):

    def __init__(self):
        super(Adition, self).__init__()


class Substraction(BinaryExpression):

    def __init__(self):
        super(Substraction, self).__init__()


class Product(BinaryExpression):
    
    def __init__(self):
        super(Substraction, self).__init__()


class Division(BinaryExpression):
    
    def __init__(self):
        super(Division, self).__init__()


# Boolean Expression.

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


class Use(ASTNode):

    def __init__(self, path):
        super(Use, self).__init__()
        self.path = path

