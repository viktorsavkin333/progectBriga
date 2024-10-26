from bottle import Bottle, run, request, response
import smtplib
import uuid
from email.mime.text import MIMEText

app = Bottle()

# Route to display the registration form
@app.route('/')
def registration_form():
    return '''
        <form action="/register" method="POST">
            Email: <input type="email" name="email" required />
            <input type="submit" value="Register" />
        </form>
    '''

# Route to handle registration
@app.route('/register', method='POST')
def register():
    email = request.forms.get('email')
    token = str(uuid.uuid4())  # Generate a unique token

    # Here you would typically save the email and token in a database

    # Send confirmation email
    send_confirmation_email(email, token)

    return "Registration successful! Please check your email to confirm your account."

def send_confirmation_email(to_email, token):
    from_email = 'e66929828@gmail.com'
    password = 'jirv akjk jrfy ifaj'

    subject = "Confirm your account"
    body = f"Click the link to confirm your account: http://localhost:8080/confirm/{token}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Включаем шифрование
            server.login(from_email, password)
            server.send_message(msg)
        print("Confirmation email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Route to confirm the account
@app.route('/confirm/<token>')
def confirm_account(token):
    # Here you would typically check if the token is valid and associated with an email
    # For this example, we'll just simulate successful confirmation:
    
    # You should implement logic to check the token against your database here.
    
    return f"Your account has been confirmed with token: {token}"

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080)