import logging
import sys
from customHandler import LevelHandler

def CreateLogger(name):
    logger = logging.getLogger(name)
    handler = LevelHandler()
    formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel("DEBUG")
    logger.addHandler(handler)
    return logger

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")

if __name__ == '__main__':
    logger = CreateLogger("Calculate")
    Calculate()