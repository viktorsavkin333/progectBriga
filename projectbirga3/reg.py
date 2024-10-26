from bottle import run, request, response, route
import sqlite3
import datetime
from progectbirg1.message_1 import message
import random

# Хранение кодов подтверждения
user_codes = dict()

# Подключение к базе данных
db = sqlite3.connect('../../../../Downloads/db1.db')
sql = db.cursor()
sql.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)
''')
db.commit()


# Страница регистрации
@route('/registration')
def registration_form():
    return '''
        <form action="/register" method="POST">
            Username: <input type="text" name="username" required />
            Email: <input type="email" name="email" required />
            Password: <input type="password" name="password" required />
            <input type="submit" value="Register" />
        </form>
    '''


def save_cookies(username: str, email: str, password: str):
    # Устанавливаем срок действия куки на 30 дней
    
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)  # DEPRECATED
    # expires = datetime.datetime.now(datetime.datetime.utcnow()) + datetime.timedelta(days=30)

    response.set_cookie("user_name", username, secret="your_secret_key", expires=expires)
    response.set_cookie("user_email", email, secret="your_secret_key", expires=expires)
    response.set_cookie("user_password", password, secret="your_secret_key", expires=expires)


def get_cookies() -> tuple[str, str, str]:  # returns username, email, password
    username = request.get_cookie("user_name", secret="your_secret_key")
    email = request.get_cookie("user_email", secret="your_secret_key")
    password = request.get_cookie("user_password", secret="your_secret_key")

    return username, email, password


@route('/register', method='POST')
def register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    email = request.forms.get('email')

    save_cookies(username, email, password)

    code = random.randint(1000, 9999)  # Генерируем код(4 символа)
    user_codes[email] = code  # Сохраненяем код для будущей проверки

    message('e669298289@gmail.com','dqry zkkq xxdu aoam', email, code) # Заускаем функцию которая отправляет письмо на указанную почту
    print(code)

    return f'Код подтверждения отправлен на {email}. <a href="/verify">Проверить код</a>'


def save_user_to_db(username: str, password: str):
    # Проверка наличия логина в базе данных
    sql.execute("SELECT * FROM users WHERE username = ?", (username,))
    if sql.fetchone():
        return "Username already exists. Please log in instead."

    # Сохранение пользователя в базе данных
    sql.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password))
    db.commit()


@route('/verify', method=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        username, email, password = get_cookies()
        code = request.forms.get('code')

        print(email, code)

        if int(user_codes[email]) == int(code):
            del user_codes[email]  # Удаление кода после успешной проверки

            result = save_user_to_db(username, password)
            if result is not None:  # возникла ошибка
                return result

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


# Страница авторизации
@route('/login')
def login_form():
    error_message = request.query.error or ""  # Получаем сообщение об ошибке из параметров запроса
    return f'''
        <form action="/login_submit" method="POST">
            Username: <input type="text" name="username" required />
            Password: <input type="password" name="password" required />
            <input type="submit" value="Log In" />
        </form>
        {f"<p>{error_message}</p>" if error_message else ""}
    '''

@route('/login_submit', method='POST')
def login_submit():
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Проверка наличия логина в базе данных
    sql.execute("SELECT * FROM users WHERE username = ?", (username,))
    
    user = sql.fetchone()
    
    if user:
        # Если логин существует, проверяем пароль
        if user[2] == password:  # user[2] - это пароль
            return f'Welcome back, {username}!'
        else:
            return login_form() + "?error=Invalid password. Please try again."
    
    return login_form() + "?error=Username not found. Please create an account."


if __name__ == '__main__':
    run(host='localhost', port=8080)
