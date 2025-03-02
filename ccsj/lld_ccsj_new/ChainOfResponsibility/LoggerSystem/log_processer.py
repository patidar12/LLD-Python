class LogProcessor:
    INFO: int = 1
    DEBUG: int = 2
    ERROR: int = 3
    def __init__(self, next_processor):
        self.next_processor: LogProcessor = next_processor
    
    def log(self, log_level, message):
        if self.next_processor:
            self.next_processor.log(log_level, message)
