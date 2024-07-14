import sqlite3

global enter 


global db
global sql

db = sqlite3.connect('db.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    diamond INTEGER,
    airon INTEGER
)""")

def login():
    global user_login, user_password
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("Такого пользователя не существует")
        main(False)
    else:
        registred = True
        sql_update_query = f"""UPDATE users set diamond = diamond+1 WHERE login = {user_login}"""
        allselect = f"""SELECT * FROM users WHERE login={user_login}"""
        sql.execute(allselect)
        records = sql.fetchall()
        print(records)
        print(type(records))
        print(records[0][-1])
        sql.execute(sql_update_query)
        db.commit()
        print("Запись успешно обновлена")
        main(True)

def reg():
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")
    diamond = 100
    airon = 0
    abc(user_login, user_password, diamond, airon)

def main(registred):
        if registred == False:
            help = "Список команд: /help - Команды, /new_user - Регистрация, /login - Вход"
            print(help)
            enter = input("Введите команду: ")
            if enter == '/help':
                print(help)
            elif enter == '/new_user':
                reg()
            elif enter == '/login':
                login()
            else:
                print('Неверная команда')
                main()
        if registred == True:
            help = "Список команд: /help - Команды, /user - Профиль, /birsh - Перейти на биржу"
            print(help)
            enter = input("Введите команду: ")
            if enter == '/help':
                print(help)
            elif enter == '/user':
                user()
            else:
                print('Неверная команда')
                main()

def abc (user_login, user_password, diamond, airon):
        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (user_login, user_password, diamond, airon))
            db.commit()
            print('Вы успешно зарегестрированны')
            main(False)
        else:
            print('Такая учетная запись уже существует')
            main(False)

def user():
    allselect = f"""SELECT * FROM users WHERE login={user_login}"""
    sql.execute(allselect)
    records = sql.fetchall()
    print(records)
    print(type(records))
    print(records[0][-1])
    main(True)
main(False)