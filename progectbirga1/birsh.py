import sqlite3
import hashlib
from pochta import email, password
import smtplib
import random

global enter 
print(email)
print(password)

global db
global sql

db = sqlite3.connect('db.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    email TEXT
    diamond INTEGER,
    airon INTEGER
)""")

def login():
    global user_login, user_password
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")
    user_password = hash256(user_password)
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}' AND password = '{user_password}'")
    if sql.fetchone() is None:
        print("Такого пользователя не существует")
        main(False)
    else:
        registred = True
        print("Вы успешно авторизованны")
        main(True)

def reg():
    user_login = input("Введите логин: ")
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    user_password = input("Введите пароль: ")
    user_password = hash256(user_password)
    print(user_password)
    if user_password == '' or user_login == '':
        print('Логин или пароль не может быть пустым')
        reg()
    user_email = input("Введите вашу почту: ")
    message(user_email)
    diamond = 100
    airon = 0
    abc(user_login, user_password, diamond, airon)

def main(registred):
        if registred == False:
            help = "Список команд: /leave - Выход, /new_user - Регистрация, /login - Вход"
            print(help)
            enter = input("Введите команду: ")
            if enter == '/leave':
                print()
            elif enter == '/new_user':
                reg()
            elif enter == '/login':
                login()
            else:
                print('Неверная команда')
                main(False)
        if registred == True:
            help = "Список команд: /leave - Выход, /user - Профиль, /birsh - Перейти на биржу"
            print(help)
            enter = input("Введите команду: ")
            if enter == '/leave':
                main(False)
            elif enter == '/user':
                user()
            elif enter == '/birsh':
                birsh()
            else:
                print('Неверная команда')
                main(True)

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
    allselect = f"""SELECT * FROM users WHERE login = '{user_login}' """
    sql.execute(allselect)
    records = sql.fetchall()
    print('Ваш логин: ', records[0][0])
    print('Ваше кол-во алмазов: ', records[0][2])
    print('Ваше кол-во железа: ', records[0][3])
    main(True)



def birsh():
    a = 0
    allironselected = """SELECT airon FROM users WHERE login= "bank" """
    sql.execute(allironselected)
    alliron1 = sql.fetchall()
    alliron = alliron1[0][0]
    proveralliron = 0
    num1 = int(input('Введите что вы хотите купить от 1 до 1 (0 для выхода): '))
    if num1 == 1:
        diamondselected = f"""SELECT diamond FROM users WHERE login={user_login}"""
        sql.execute(diamondselected)
        diamondi0 = sql.fetchall()
        diamondi1 = diamondi0[0][0]
        print('Вы выбрали железо')
        print(f'Сейчас у вас {diamondi1} алмазов')
        kol = int(input('Введите количество(в алмазах)'))
        if kol > diamondi1:
            print('У вас не хватает алмазов')
            birsh()
        else:
            for i in range(kol):
                allironselected = """SELECT airon FROM users WHERE login= "bank" """
                sql.execute(allironselected)
                alliron1 = sql.fetchall()
                alliron = alliron1[0][0]
                proveralliron += birshiron(alliron)
            if proveralliron > alliron:
                print('В банке не хватает железа')
                birsh()
            else:
                for i in range(kol):
                    allironselected = """SELECT airon FROM users WHERE login= "bank" """
                    sql.execute(allironselected)
                    alliron1 = sql.fetchall()
                    alliron = alliron1[0][0]
                    birshiron(alliron)
                    a += (1 * birshiron(alliron))
                print(f'Количества железа за {kol} алмазов: {a}')
                yesornoo = int(input('Согласны продолжитьть? (1/0)'))
                if yesornoo == 1:
                    try:
                        sql.execute('BEGIN TRANSACTION')
                        for i in range(kol):
                            allironselected = """SELECT airon FROM users WHERE login= "bank" """
                            sql.execute(allironselected)
                            alliron1 = sql.fetchall()
                            alliron = alliron1[0][0]
                            birshiron(alliron)
                            sql_update_diamond = f"""UPDATE users set diamond = diamond-1 WHERE login = {user_login}"""
                            sql_update_airon = f"""UPDATE users set airon = airon+(1*{birshiron(alliron)}) WHERE login = {user_login} """
                            sql_update_bankairon = f"""UPDATE users set airon = airon-(1*{birshiron(alliron)}) WHERE login = "bank" """
                            sql.execute(sql_update_diamond)
                            sql.execute(sql_update_airon)
                            sql.execute(sql_update_bankairon)
                        db.commit()
                        db.commit()
                        db.commit()
                        db.commit()
                        print("Покупка завершенна")

                    except:
                        sqlite3.Error
                        # Rollback the transaction in case of an error
                        db.rollback()

                    
                    finally:
                        # Close the cursor and connection
                        birsh()
                                
                else:
                    birsh()
    else:
        main(True)
        #print(balance)




def birshiron(alliron):
    if alliron <= 50:
        priseiron = 1
    elif 500 >= alliron >= 51:
        priseiron = 5
    elif 2500 >= alliron >= 501:
        priseiron = 10
    elif 10000 >= alliron >= 2501:
        priseiron = 20
    elif 50000 >= alliron >= 10001:
        priseiron = 40
    return priseiron

def message(user_email):
    smtp_server = "smtp.gmail.com"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # обновляем соединение с использованием TLS-шифровани
    server.login(email, password)
    from_email = email
    to_email = user_email
    a = random.randint(1000, 9999)
    server.sendmail(from_email, to_email, f"Subject: {a}")

    c = int(input('Введите число отправленное вам на почту(так-же проверьте папку спам) '))

    if c == a:
        print('OK')
    else:
        print('NOT OK')




def hash256(text):
    return hashlib.sha256(text.encode()).hexdigest()


if __name__ == "__main__":
    main(False)

# добавить хеши 
# проверять уникальность логинов 