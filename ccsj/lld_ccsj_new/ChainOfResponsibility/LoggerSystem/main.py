from info_log_processor import InfoLogger
from debug_log_processor import DebugLogger
from error_log_processor import ErrorLogger
from log_processer import LogProcessor

class Logger:
    def __init__(self):
        self.logger = InfoLogger(DebugLogger(ErrorLogger(None)))
    def log(self, log_level, message):
        self.logger.log(log_level, message)

logger = Logger()
logger.log(LogProcessor.INFO, "Info level message")
logger.log(LogProcessor.ERROR, "Error level message")
logger.log(LogProcessor.DEBUG, "Debug level message")
logger.log(4, "Unknown level message")

