import smtplib
import random

from pochta import email, password

def message(user_email):
    smtp_server = "smtp.gmail.com"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # обновляем соединение с использованием TLS-шифровани
    a = False
    while a != True:
        server.login(email, password)
        from_email = email
        to_email = user_email
        a = random.randint(1000, 9999)
        server.sendmail(from_email, to_email, f"Subject: {a}")

        c = int(input('Введите число отправленное вам на почту(так-же проверьте папку спам) '))

        if c == a:
            a = True
            return 
        else:
            print('NOT OK')