class BaseException(Exception):
    MESSAGE = "Something went wrong..."
    def __init__(self, message: str = None, **kwargs):
        message = message or self.MESSAGE
        super().__init__(message, **kwargs)
    


class InvalidShape(BaseException):
    MESSAGE = "Invalid shape. Please provide correct shape type."
    def __init__(self, message: str = None, **kwargs):
        message = message or self.MESSAGE
        super().__init__(message, **kwargs)
    


    