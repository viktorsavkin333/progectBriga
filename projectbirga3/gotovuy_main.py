from bottle import Bottle, run, request, response
import datetime
import sqlite3
import smtplib
import random
from progectbirg1.message_1 import message
from progectbirg1.login import login
from progectbirg1.reg import reg

app = Bottle()

db = sqlite3.connect('db.db')
sql = db.cursor()

user_email = ''

# Route to display the form
@app.route('/avtorization')
def form():
    return '''
        <form action="/avt_submit" method="POST">
            Username: <input type="text" name="username" required />
            Password: <input type="password" name="password" required />
            <input type="submit" value="Save" />
        </form>
    '''

def form2():
    return '''
        <form action="/avt_submit" method="POST">
            Username: <input type="text" name="username" required />
            Password: <input type="password" name="password" required />
            <input type="submit" value="Save" />
            <div Неверный логин/>
        </form>
    '''

@app.route('/avt_submit', method='POST')
def submite():
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Here you would typically validate the username and password
    if username == "admin" and password == "password":  # Simple check for demonstration
        # Set a cookie to indicate that the user is logged in with an expiration of 30 days
        expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        response.set_cookie("session", (username, password), secret="your_secret_key", expires=expires)
        return f'You are logged in as {username}.'
    else:
        return 'Invalid credentials. Please try again.'

@app.route('/regestration')
def regestration():
    return '''
        <form action="/reg_sumbit" method="POST">
            Username: <input type="text" name="username" required />
            Password: <input type="password" name="password" required />
            <input type="submit" value="Save" />
        </form>
    '''

@app.route('/reg_sumbit', method='POST')
def verdict():
    username = request.forms.get('username')
    password = request.forms.get('password')
    # user_email = request.forms.get('email')
    # Email: <input inputmode="email" type="email" name="email" required />
    # user_email == 've-savkin@yandex.ru'
    # добавить связь с бд
    if password == '123' and username == '123':
        return '''
        <form action="/email_sumbit" method="POST">
            Email: <input inputmode="email" type="email" name="email" required />
            <input type="submit" value="Send Message" />
        </form>
    '''

@app.route('/email_sumbit', method='POST')
def proverca():
    # ujoj ouvt wond xyxk - password
    user_email = request.forms.get('email')
    smtp_server = "smtp.gmail.com"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # обновляем соединение с использованием TLS-шифровани
    a = False
    while a != True:
        server.login(email, password)
        from_email = email
        to_email = user_email
        global code
        code = random.randint(1000, 9999)
        server.sendmail(from_email, to_email, f"Subject: {code}")
        code_funck(code)
    return '''
    <form action="/code_sumbit" method="POST">
        code: <input inputmode="number" type="code" name="code" required />
        <input type="submit" value="Send Code" />
    </form>
    '''

@app.route('code_sumbit', method='POST')
def code_funck(code):
    code_get = request.forms.get('code')
    if code_get == code:
        return f"ЕБАНАТ?"



if __name__ == '__main__':
    run(app, host='localhost', port=8080)