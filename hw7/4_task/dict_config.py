from customHandler import LevelHandler

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
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "logfile.log",
            "mode": "a"
        },
        "level":{
            "()": LevelHandler,
            "level": "DEBUG",
            "formatter": "base",
        }
    },
    "loggers": {
        "Calculate": {
            "level": "DEBUG",
            "handlers": ["level"]
        }
    },

}