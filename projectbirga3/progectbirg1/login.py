from progectbirg1.coder1 import coder_password
import sqlite3

db = sqlite3.connect('../db.db')
sql = db.cursor()

def login():
    global user_login, user_password
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")
    user_password = coder_password(user_password)
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}' AND password = '{user_password}'")
    if sql.fetchone() is None:
        print("Такого пользователя не существует")
        return False
    else:
        registred = True
        print("Вы успешно авторизованны")
        return True