from flask import Flask
from typing import List

app = Flask(__name__)


@app.route('/max_number/<path:number_string>')
def max_number(number_string: str):
    numbers: List[int] = [int(num) for num in number_string.split('/') if num.isdigit()]

    if numbers:
        max_num: int = max(numbers)
        return f"Максимальное число: {max_num}"
    else:
        return "Неверный формат чисел в запросе."


if __name__ == '__main__':
    app.run(debug=True)
