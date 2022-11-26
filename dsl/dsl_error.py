class ErrorType:
    """Base class for all error types."""
    def __init__(self):
        self.message = 'Base error'

    def __str__(self):
        return self.message


class DSLError:
    """Base class for all DSL errors."""
    def __init__(self, line, pos, error_type: ErrorType):
        self.line = line
        self.pos = pos
        self.error_type = error_type

    def __str__(self):
        return f'{self.error_type}: {self.error_type.message} at line {self.line}, pos {self.pos}'


# cada vez que tengas un nuevo tipo de error que manejar, creas una nueva clase y le define el mensaje
class NameError(ErrorType):
    """Error for undefined variables."""
    def __init__(self):
        self.message = 'Undefined variable'

class TypeError(ErrorType):
    """Error for type mismatch."""
    def __init__(self):
        self.message = 'Type mismatch'
