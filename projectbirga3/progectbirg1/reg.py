import sqlite3
from progectbirg1.coder1 import coder_password
import smtplib
import random
from progectbirg1.message_1 import message


db = sqlite3.connect('db.db')
sql = db.cursor()

user_email = ''

def reg(user_login, user_password, user_email):
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    user_password = coder_password(user_password)
    print(user_password) 
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





