from bottle import Bottle, run, request, response, route
import sqlite3
from progectbirg1.message_1 import message
import random
import datetime


# Хранение кодов подтверждения 
user_codes = dict()

@route('/')
def index():
    return '''
        <form action="/send_code" method="POST">
            Email: <input type="email" name="email" required />
            <input type="submit" value="Отправить код" />
        </form>
    '''


@route('/send_code', method='POST')
def send_code():
    email = request.forms.get('email')
    code = random.randint(1000, 9999) # Генерируем код(4 символа)
    user_codes[email] = code  # Сохраненяем код для будущей проверки
    # set cookie
    message('e669298289@gmail.com','dqry zkkq xxdu aoam', email, code) # Заускаем функцию которая отправляет письмо на указанную почту
    set_cookie(email)
    return f'Код подтверждения отправлен на {email}. <a href="/verify">Проверить код</a>'

def set_cookie(email):
    # Устанавливаем срок действия куки на 30 дней
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    response.set_cookie("user_email", email, secret="your_secret_key", expires=expires)

@route('/verify', method=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        # email = get.cookie
        email = request.get_cookie("user_email", secret="your_secret_key")
        code = request.forms.get('code')
        print(email, code)
        if int(user_codes[email]) == int(code):
            del user_codes[email]  # Удаление кода после успешной проверки
            return 'Почта успешно подтверждена!'
        else:
            return 'Неверный код подтверждения!'

    return '''
        <form action="/verify" method="POST">
            Код: <input type="text" name="code" required />
            <input type="submit" value="Подтвердить" />
        </form>
    '''
            # Email: <input type="email" name="email" required />

if __name__ == '__main__':
    run(host='localhost', port=8080)