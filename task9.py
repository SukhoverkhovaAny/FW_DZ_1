# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/cloth/')
def cloth():
    _clothes = [{'model' : 'Блуза шелковая',
                'color' : 'Белый',
                'size': '42-44',
                'price': '2000.0',
                },
                {'model' : 'Брюки клёш',
                 'color' : 'Черный',
                'size': '42-48',
                'price': '3000.0',
                },
                {'model' : 'Пальто',
                 'color' : 'Оливковый',
                'size': '42-48',
                'price': '15000.0',
                }, ]
    context = {'clothes' : _clothes,
               'title' : 'Одежда'}
    return render_template('cloth.html', **context)

@app.route('/shoes/')
def shoes():
    _shoes = [{'model' : 'Сапоги',
                'color' : 'Черный',
                'size': '36-42',
                'price': '2999.0',
                },
                {'model' : 'Туфли',
                 'color' : 'Бежевый',
                'size': '35-40',
                'price': '1750.0',
                },
                {'model' : 'Кроссовки',
                 'color' : 'Белый',
                'size': '35-40',
                'price': '7500.0',
                }, ]
    context = {'shoes' : _shoes,
               'title' : 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/access/')
def accessories():
    _accessories = [{'model' : 'Серьги',
                'material' : 'Золото',
                'price': '39000.0',
                },
                {'model' : 'Кольцо',
                'material' : 'Золото',
                'price': '17550.0',
                },
                {'model' : 'Браслет',
                'material' : 'Серебро',
                'price': '4590.0',
                }, 
                {'model' : 'Цепочка',
                'material' : 'Серебро',
                'price': '9300.0',
                }, ]
    context = {'accessories' : _accessories,
               'title' : 'Аксессуары'}
    return render_template('accessories.html', **context)

if __name__ == '__main__':
    app.run(debug=True)