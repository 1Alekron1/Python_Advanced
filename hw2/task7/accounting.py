from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

storage = defaultdict(lambda: defaultdict(int))


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        if len(date) > 8:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Неверный формат даты'}), 400

    storage[year][month] += number
    storage[year]['total'] += number

    return "Затраты добавлены."


@app.route('/calculate/<int:year>')
def calculate_year(year):
    if year in storage:
        return f"Суммарные траты за {year} год: {storage[year]['total']}"
    else:
        return "Нет данных о затратах за указанный год."


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    if year in storage and month in storage[year]:
        return f"Суммарные траты за {month}.{year}: {storage[year][month]}"
    else:
        return "Нет данных о затратах за указанный месяц."


if __name__ == '__main__':
    app.run(debug=True)
