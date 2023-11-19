# Задание №8
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/about/')
def about():
    context = {
        'title' : 'О нас',
        'date_of_creation': '18.11.2023',
        'creator': 'Тайный питонист'
    }
    return render_template('about.html', **context)

@app.route('/contacts/')
def contacts():
    context = {
        'title' : 'Контакты',
        'number' : '8-999-777-66-55',
        'adress' : 'planet Earth',
        'e_mail' : 'secret_creator@mail.ru',
    }
    return render_template('contacts.html', **context)

if __name__ == '__main__':
    app.run(debug=True)