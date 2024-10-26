from bottle import Bottle, run, request, response
import datetime

app = Bottle()

# Route to display the form
@app.route('/')
def form():
    return '''
        <form action="/submit" method="POST">
            Username: <input type="text" name="username" required />
            Password: <input type="password" name="password" required />
            Scan Box: <input type="text" name="package" required />
            Scan Item: <input type="text" name="sample" required />
            <input type="submit" value="Save" />
        </form>
    '''

# Route to handle form submission
@app.route('/submit', method='POST')
def submit():
    username = request.forms.get('username')
    password = request.forms.get('password')
    package = request.forms.get('package')
    sample = request.forms.get('sample')

    # Here you would typically validate the username and password
    if username == "admin" and password == "password":  # Simple check for demonstration
        # Set a cookie to indicate that the user is logged in with an expiration of 30 days
        expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        response.set_cookie("session", (username, password), secret="your_secret_key", expires=expires)
        return f'You scanned Box: {package} and Item: {sample}. You are logged in as {username}.'
    else:
        return 'Invalid credentials. Please try again.'

# Route to check if the user is logged in
@app.route('/check-login')
def check_login():
    session_cookie = request.get_cookie("session", secret="your_secret_key")
    return f"You are logged in {session_cookie}"

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080)