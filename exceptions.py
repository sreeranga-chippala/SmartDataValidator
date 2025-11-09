class DataValidationError(Exception):
    pass
class MissingValueError(DataValidationError):
    def __init__(self, field):
        message=f"Missing field:{field}"
        super().__init__(message)
class InvalidTypeError(DataValidationError):
    def __init__(self,field,expected,actual):
        message=f"Invalid type for {field}, expected {expected} but actual is {actual}"
        super().__init__(message)
class OutOfRangeError(DataValidationError):
    def __init__(self, field, value, min_value, max_value):
        message = f"The value {value} is out of range . The minimum is {min_value} and maximum is {max_value}"
        super().__init__(message)
