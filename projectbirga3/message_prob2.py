from bottle import Bottle, run, request, redirect, template
import smtplib
import random
import string

app = Bottle()

# Хранение кодов подтверждения (в реальном приложении используйте базу данных)
verification_codes = {}

def send_email(recipient, code):
    sender = 'e669298289@gmail.com'  # Ваш email
    password = 'dqry zkkq xxdu aoam'  # Ваш пароль
    subject = 'Код подтверждения'
    body = f'Ваш код подтверждения: {code}'

    message = f'Subject: {subject}, {body}'

    with smtplib.SMTP('smtp.example.com', 587) as server:  # Замените на ваш SMTP сервер
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message)

@app.route('/')
def index():
    return '''
        <form action="/send_code" method="POST">
            Email: <input type="email" name="email" required />
            <input type="submit" value="Отправить код" />
        </form>
    '''

@app.route('/send_code', method='POST')
def send_code():
    email = request.forms.get('email')
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # Генерация кода из 6 символов
    verification_codes[email] = code  # Сохранение кода для проверки

    send_email(email, code)  # Отправка кода на email
    return f'Код подтверждения отправлен на {email}. <a href="/verify">Проверить код</a>'

@app.route('/verify', method=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        email = request.forms.get('email')
        code = request.forms.get('code')

        if email in verification_codes and verification_codes[email] == code:
            del verification_codes[email]  # Удаление кода после успешной проверки
            return 'Почта успешно подтверждена!'
        else:
            return 'Неверный код подтверждения!'

    return '''
        <form action="/verify" method="POST">
            Email: <input type="email" name="email" required />
            Код: <input type="text" name="code" required />
            <input type="submit" value="Подтвердить" />
        </form>
    '''

if __name__ == '__main__':
    run(app, host='localhost', port=8080)