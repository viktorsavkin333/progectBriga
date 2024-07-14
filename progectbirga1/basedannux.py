import sqlite3
from random import randint

global enter
help = "Command List: /help - Show full list of commands, /new_user - Create new user, /login - Login to user, /casino - Play casino"

global db
global sql

db = sqlite3.connect('data.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    birthday_year BEGIN,
    birthday_month BEGIN,
    user_birthday_day BEGIN,
    gender TEXT,
    cash BEGIN
)""")
while True:
    def login():
        user_login = input("Enter login: ")
        user_password = input("Enter password: ")

        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if sql.fetchone() is None:
            print("This user does not exist")
            main()
        elif sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'") != sql.fetchone() is None:
            print('1')

    def reg():
            user_login = input("Enter login: ")
            user_password = input("Enter password: ")
            user_birthday_year = int(input("Enter birthday year: "))
            user_birthday_month = int(input("Enter birthday month: "))
            user_birthday_day = int(input("Enter birthday day: "))
            user_gender = input("Enter gender (f-female or m-male): ")
            if user_birthday_year > 1897 and user_birthday_year < 2022:
                if user_birthday_month > 0 and user_birthday_month < 13:
                    if user_birthday_day > 0 and user_birthday_day < 32:
                        if user_gender == 'f' or user_gender == 'm':
                            abc(user_login, user_password, user_birthday_year, user_birthday_month, user_birthday_day,
                                user_gender)
            else:
                print('Carefully check the correctness of the data you entered')
                reg()

    db.commit()
    def main():
        print(help)
        enter = input("Enter the command: ")
        if enter == '/help':
            print(help)
        elif enter == '/new_user':
            reg()
        elif enter == '/login':
            login

    def abc (user_login, user_password,user_birthday_year, user_birthday_month, user_birthday_day, user_gender):
        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", (user_login, user_password, user_birthday_year, user_birthday_month, user_birthday_day, user_gender, 0))
            db.commit()
            print('You have successfully registered')
            main()
        else:
            print('Such a record already exists')
            main()

main()