from log_processer import LogProcessor

class ErrorLogger(LogProcessor):
    def __init__(self, next_processor):
        super().__init__(next_processor)
    
    def log(self, log_level, message):
        if log_level == LogProcessor.ERROR:
            print(f"Error: {message}")
        else:
            super().log(log_level, message)
