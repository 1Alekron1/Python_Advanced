from flask import Flask
import os

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)

    try:
        with open(abs_path, 'r') as file:
            content = file.read(size)
            result_size = len(content)
            file_info = f"<b>{abs_path}</b> {result_size}<br>"
            return f"{file_info}\n{content}"
    except FileNotFoundError:
        return "Файл не найден."


if __name__ == '__main__':
    app.run(debug=True)
