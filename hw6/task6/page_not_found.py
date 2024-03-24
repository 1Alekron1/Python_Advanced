from flask import Flask, render_template_string
from flask import request, redirect, url_for

app = Flask(__name__)


# Декоратор для получения списка всех доступных страниц
def available_pages_decorator(func):
    def wrapper(*args, **kwargs):
        pages = [rule for rule in app.url_map.iter_rules() if rule.endpoint != 'static']
        return func(pages)

    return wrapper


# Обработчик ошибки 404
@app.errorhandler(404)
@available_pages_decorator
def page_not_found(pages):
    page_links = ''.join(
        f'<li><a href="{url_for(page.endpoint, **(page.defaults or {}))}">{page.endpoint}</a></li>' for page in pages)
    return render_template_string(
        f'<h1>Page Not Found</h1>'
        f'<p>The requested URL was not found on the server.</p>'
        f'<p>Available pages:</p>'
        f'<ul>{page_links}</ul>'
    ), 404


# Эндпоинт для домашней страницы
@app.route('/')
def home():
    return '<h1>Welcome to the Home Page</h1>'


# Эндпоинт для страницы "О нас"
@app.route('/about')
def about():
    return '<h1>About Us</h1>'


# Эндпоинт для страницы "Контакты"
@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'


if __name__ == '__main__':
    app.run(debug=True)
