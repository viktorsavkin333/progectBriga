from bottle import Bottle, run, request, response
import datetime
import random


app = Bottle()

# Route to set a cookie
@app.route('/set-cookie')
def set_cookie():
    # Устанавливаем срок действия куки на 30 дней
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    response.set_cookie("username", random.randint(1,100000), secret="your_secret_key", expires=expires)
    return "Cookie has been set!"

# Route to get the cookie
@app.route('/get-cookie')
def get_cookie():
    username = request.get_cookie("username", secret="your_secret_key")
    return f"Hello {username}!" if username else "No cookie found."

@app.route('/submit', method='POST')
def submit():
    username = request.forms.get('username')
    password = request.forms.get('password')

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080)