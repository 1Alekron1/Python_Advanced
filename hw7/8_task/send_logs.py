import logging
from dict_config import dict_config
import logging.config

def CreateLogger(name):
    logger = logging.getLogger(name)
    logging.config.dictConfig(dict_config)
    return logger

def func():
    logger.info("INFO")
    logger.debug("DEBUG")
    logger.error("ERROR")
    logger.warning("WARNING")

if __name__ == '__main__':
    logger = CreateLogger("logger")
    func()