from LogProcessor import LogProcessor

class DebugLogger(LogProcessor):

    def __init__(self, next_logger):
        super().__init__(next_logger)
    
    def log(self, log_level: int, message: str):
        if log_level == self.DEBUG:
            print("DEBUG: ", message)
        else:
            super().log(log_level, message)
