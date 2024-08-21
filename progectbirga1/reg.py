import sqlite3
from coder import coder
import smtplib
import random
from message_1 import message


db = sqlite3.connect('db.db')
sql = db.cursor()

user_email = ''

def reg(avtorization):
    if avtorization == False:
        global user_login, user_password, user_email
        user_login = input("Введите логин: ")
        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        user_password = input("Введите пароль: ")
        user_password = coder(user_password)
        print(user_password)
        if user_password == '' or user_login == '':
            print('Логин или пароль не может быть пустым')
            reg(False)
        user_email = input("Введите вашу почту: ")
        message(user_email)
        abc(user_login, user_password, user_email)

def abc (user_login, user_password, user_email):
        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, user_email))
            db.commit()
            sql.execute(f"INSERT INTO diamond VALUES (?, ?)", (user_login, 100))
            db.commit()
            sql.execute(f"INSERT INTO iron VALUES (?, ?)", (user_login, 0))
            db.commit()
            sql.execute(f"INSERT INTO gold VALUES (?, ?)", (user_login, 0))
            db.commit()
            sql.execute(f"INSERT INTO emerald VALUES (?, ?)", (user_login, 0))
            db.commit()
            sql.execute(f"INSERT INTO quartz VALUES (?, ?)", (user_login, 0))
            db.commit()
            sql.execute(f"INSERT INTO nezerite VALUES (?, ?)", (user_login, 0))
            db.commit()
            print('Вы успешно зарегестрированны')
        else:
            print('Такая учетная запись уже существует')





