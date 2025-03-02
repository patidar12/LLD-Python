class BaseException(Exception):
    MESSAGE = "Somethins went worng..."
    def __init__(self, message: str = None, **kwargs):
        message = message or self.MESSAGE
        super().__init__(message, **kwargs)


class InvalidShape(BaseException):
    MESSAGE = "Invalid shape. Please provide correct shape type."
    def __init__(self, message: str = None, **kwargs):
        message = self.MESSAGE or message
        super().__init__(message, **kwargs)
        '''
        if multiple inheritance then we can use: BaseException.__int__(self, message, **kwargs)
        To invoke particular class constructor.
        BaseException().__int__(message, **kwargs), this is the wrong way of intializing the base class consutructor.
        Because of we are creating a new object.
        '''
