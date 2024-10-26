import smtplib
import random

# from progectbirg1.pochta import email, password

def message(email, password, user_email, code):
    smtp_server = "smtp.gmail.com"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # обновляем соединение с использованием TLS-шифровани
    server.login(email, password)
    from_email = email
    to_email = user_email
    server.sendmail(from_email, to_email, f"Subject: {code}")
    # proverca_coda(a)

