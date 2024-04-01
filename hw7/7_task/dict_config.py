import logging


class AsciiFilter(logging.Filter):
    def filter(self, record):
        return 1 if record.message.encode().isascii() else 0

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calculate.log"
        },
        "timed": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calculate.log",
            "when": "H",
            "interval": 10,
            "backupCount": 0,
        }
    },
    "loggers": {
        "Calculate": {
            "level": "DEBUG",
            "handlers": ["file"],
            "filter": AsciiFilter
        }
    },

}