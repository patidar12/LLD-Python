from InfoLogProcessor import InfoLogger
from DebugLogProcessor import DebugLogger
from ErrorLogProcessor import ErrorLogger
from LogProcessor import LogProcessor

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

