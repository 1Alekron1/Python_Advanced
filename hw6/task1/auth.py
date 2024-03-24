import logging

# Настройка формата сообщения для логгера
formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%H:%M:%S')

# Создание логгера
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Создание обработчика для записи в файл stderr.txt
file_handler = logging.FileHandler('stderr.txt', mode='a')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

# Примеры использования логгера
logger.info('This is an INFO message')
logger.warning('This is a WARNING message')
