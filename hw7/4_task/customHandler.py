import logging
from re import match


class LevelHandler(logging.Handler):
    def __init__(self, mode = "a"):
        super().__init__()
        self.debug_file = "calc_debug.log"
        self.err_file = "calc_error.log"
        self.info = "calc_info.log"
        self.mode = mode
    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        file_name = "calc_ERRORS_handler.log"
        level = record.levelno
        if level == logging.DEBUG:
            file_name = "calc_debug.log"
        elif level == logging.ERROR:
            file_name = "calc_error.log"
        elif level == logging.INFO:
            file_name = "calc_info.log"
        with open(file_name, mode=self.mode) as f:
            f.write(message + '\n')