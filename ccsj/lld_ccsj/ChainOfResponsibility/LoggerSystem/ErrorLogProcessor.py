from LogProcessor import LogProcessor

class ErrorLogger(LogProcessor):

    def __init__(self, next_logger):
        super().__init__(next_logger)
    
    def log(self, log_level: int, message: str):
        if log_level == self.ERROR:
            print("ERROR: ", message)
        else:
            super().log(log_level, message)
