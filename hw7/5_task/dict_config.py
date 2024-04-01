dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
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
            "handlers": ["timed"]
        }
    },

}