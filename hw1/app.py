from datetime import datetime, timedelta
from random import choice
from flask import Flask
import os
import re

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt")

CARS = ["Chevrolet", "Renault", "Ford", "Lada"]
CATS = [
    "корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин",
]

visits = 0


def get_words_list():
    with open(BOOK_FILE, "r", encoding="utf-8") as file:
        text = file.read()
    words = re.findall(r"\b\w+\b", text)
    return words


WORDS_LIST = get_words_list()


@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"


@app.route("/cars")
def cars():
    return ", ".join(CARS)


@app.route("/cats")
def cats():
    return choice(CATS)


@app.route("/get_time/now")
def time_now():
    current_time = datetime.now()
    return f"Точное время: {current_time}"


@app.route("/get_time/future")
def time_future():
    current_time = datetime.now()
    delta = timedelta(hours=1)
    current_time_after_hour = current_time + delta
    return f"Точное время через час будет: {current_time_after_hour}"


@app.route("/get_random_word")
def get_random_word():
    return choice(WORDS_LIST)


@app.route("/counter")
def counter():
    global visits
    visits += 1
    return str(visits)


def get_words_list():
    with open(BOOK_FILE, "r", encoding="utf-8") as file:
        text = file.read()
    words = re.findall(r"\b\w+\b", text)
    return words


if __name__ == "__main__":
    app.run(debug=True)
