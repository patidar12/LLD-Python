class LogProcessor:
    INFO: int = 1
    DEBUG: int = 2
    ERROR: int = 3

    def __init__(self, next_logger):
        self.next_logger = next_logger
    
    def log(self, log_level: int, message: str):
        if self.next_logger:
            self.next_logger.log(log_level, message)