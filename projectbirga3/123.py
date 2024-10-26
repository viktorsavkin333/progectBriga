from bottle import Bottle, run, request, response
import sqlite3

app = Bottle()

# Подключение к базе данных
db = sqlite3.connect('db1.db')
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
@app.route('/registration')
def registration_form():
    return '''
        <form action="/register" method="POST">
            Username: <input type="text" name="username" required />
            Password: <input type="password" name="password" required />
            <input type="submit" value="Register" />
        </form>
    '''

@app.route('/register', method='POST')
def register():
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Проверка наличия логина в базе данных
    sql.execute("SELECT * FROM users WHERE username = ?", (username,))
    if sql.fetchone():
        return "Username already exists. Please log in instead."

    # Сохранение пользователя в базе данных
    sql.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password))
    db.commit()

    return "Registration successful! You can now log in."

# Страница авторизации
@app.route('/login')
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

@app.route('/login_submit', method='POST')
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
    run(app, host='localhost', port=8080)