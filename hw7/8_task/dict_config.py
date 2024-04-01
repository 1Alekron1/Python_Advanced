import logging
from logging.handlers import HTTPHandler

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "handlers": {
        "HTTP": {
            "class": "logging.handlers.HTTPHandler",
            "host": "127.0.0.1:5000",
            "url": "/post_logs",
            "method": "POST"
        }
    },
    "loggers": {
        "logger": {
            "level": "DEBUG",
            "handlers": ["HTTP"]
        }
    },

}