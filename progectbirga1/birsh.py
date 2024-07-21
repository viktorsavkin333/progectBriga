import sqlite3
import hashlib
# poshta отдельный файл с паролем(приложения) и логином почты
from pochta import email, password
import smtplib
import random

global enter 


global db
global sql

db = sqlite3.connect('db.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    email TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS diamond (
    login TEXT,
    diamond INTEGER
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS iron (
    login TEXT,
    iron INTEGER
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS gold (
    login TEXT,
    gold INTEGER
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS emerald (
    login TEXT,
    emerald INTEGER
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS quartz (
    login TEXT,
    quartz INTEGER
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS nezerite (
    login TEXT,
    nezerite INTEGER
)""")
# Уберите кавычки один раз после того как создали бд чтобы добавить аккаунт банка
#sql.execute(f"INSERT INTO users VALUES (?, ?, ?) ", ('bank', 'bank', 'bank'))
#sql.execute(f"INSERT INTO diamond VALUES (?, ?)", ('bank', 0))
#sql.execute(f"INSERT INTO iron VALUES (?, ?)", ('bank', 10000))
#sql.execute(f"INSERT INTO gold VALUES (?, ?)", ('bank', 10000))
#sql.execute(f"INSERT INTO emerald VALUES (?, ?)", ('bank', 10000))
#sql.execute(f"INSERT INTO quartz VALUES (?, ?)", ('bank', 10000))
#sql.execute(f"INSERT INTO nezerite VALUES (?, ?)", ('bank', 10000)) 
#db.commit()
#db.commit()
#db.commit()
#db.commit()
#db.commit()
#db.commit()

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

def reg(avtorization):
    if avtorization == False:
        global user_login, user_password, user_email
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
    elif avtorization == True:
        abc(user_login, user_password, user_email)

def main(registred):
        if registred == False:
            help = "Список команд: /leave - Выход, /new_user - Регистрация, /login - Вход"
            print(help)
            enter = input("Введите команду: ")
            if enter == '/leave':
                print()
            elif enter == '/new_user':
                reg(False)
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
    num1 = int(input('Введите что вы хотите купить от 1 до 5 где: \n 1 - железо \n 2 - золото \n 3 - изумруд \n 4 - кварц \n 5 - незерит \n (0 для выхода): '))
    if num1 == 1:
        iron()
    elif num1 == 2:
        gold()
    elif num1 == 3:
        emerald()
    elif num1 == 4:
        quartz()
    elif num1 == 5:
        nezerite()
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

def birshgold(alliron):
    if alliron <= 50:
        priseiron = 0,5
    elif 500 >= alliron >= 51:
        priseiron = 2,5
    elif 2500 >= alliron >= 501:
        priseiron = 5
    elif 10000 >= alliron >= 2501:
        priseiron = 10
    elif 50000 >= alliron >= 10001:
        priseiron = 20
    return priseiron

def birshemerald(alliron):
    if alliron <= 50:
        priseiron = 0,3
    elif 500 >= alliron >= 51:
        priseiron = 1,6
    elif 2500 >= alliron >= 501:
        priseiron = 3
    elif 10000 >= alliron >= 2501:
        priseiron = 6
    elif 50000 >= alliron >= 10001:
        priseiron = 12
    return priseiron

def birshquartz(alliron):
    if alliron <= 50:
        priseiron = 2
    elif 500 >= alliron >= 51:
        priseiron = 10
    elif 2500 >= alliron >= 501:
        priseiron = 20
    elif 10000 >= alliron >= 2501:
        priseiron = 40
    elif 50000 >= alliron >= 10001:
        priseiron = 80
    return priseiron

def birshnezerite(alliron):
    if alliron <= 50:
        priseiron = 0,3
    elif 500 >= alliron >= 51:
        priseiron = 1,6
    elif 2500 >= alliron >= 501:
        priseiron = 3
    elif 10000 >= alliron >= 2501:
        priseiron = 6
    elif 50000 >= alliron >= 10001:
        priseiron = 12
    return priseiron

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
            reg(True)
        else:
            print('NOT OK')




def hash256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def iron():
    a = 0
    allironselected = """SELECT iron FROM iron WHERE login= "bank" """
    sql.execute(allironselected)
    alliron1 = sql.fetchall()
    alliron = alliron1[0][0]
    proveralliron = 0
    diamondselected = f"""SELECT diamond FROM diamond WHERE login='{user_login}'"""
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
            allironselected = """SELECT iron FROM iron WHERE login= "bank" """
            sql.execute(allironselected)
            alliron1 = sql.fetchall()
            alliron = alliron1[0][0]
            proveralliron += birshiron(alliron)
        if proveralliron > alliron:
            print('В банке не хватает железа')
            birsh()
        else:
            for i in range(kol):
                allironselected = """SELECT iron FROM iron WHERE login= "bank" """
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
                        allironselected = """SELECT iron FROM iron WHERE login= "bank" """
                        sql.execute(allironselected)
                        alliron1 = sql.fetchall()
                        alliron = alliron1[0][0]
                        birshiron(alliron)
                        sql_update_diamond = f"""UPDATE diamond set diamond = diamond-1 WHERE login = '{user_login}'"""
                        sql_update_airon = f"""UPDATE iron set iron = iron+(1*{birshiron(alliron)}) WHERE login = '{user_login}' """
                        sql_update_bankairon = f"""UPDATE iron set iron = iron-(1*{birshiron(alliron)}) WHERE login = "bank" """
                        sql.execute(sql_update_diamond)
                        sql.execute(sql_update_airon)
                        sql.execute(sql_update_bankairon)
                    db.commit()
                    db.commit()
                    db.commit()
                    db.commit()
                    print("Покупка завершенна")
                except sqlite3.Error as e:
                    print(e)
                    # Rollback the transaction in case of an error
                    print('except')
                    db.rollback()
                
                finally:
                    # Close the cursor and connection
                    birsh()
                            
            else:
                birsh()



def gold():
    a = 0
    allironselected = """SELECT gold FROM gold WHERE login= "bank" """
    sql.execute(allironselected)
    alliron1 = sql.fetchall()
    alliron = alliron1[0][0]
    proveralliron = 0
    diamondselected = f"""SELECT diamond FROM diamond WHERE login='{user_login}'"""
    sql.execute(diamondselected)
    diamondi0 = sql.fetchall()
    diamondi1 = diamondi0[0][0]
    print('Вы выбрали золото')
    print(f'Сейчас у вас {diamondi1} алмазов')
    kol = int(input('Введите количество(в алмазах)'))
    if kol > diamondi1:
        print('У вас не хватает алмазов')
        birsh()
    else:
        for i in range(kol):
            allironselected = """SELECT gold FROM gold WHERE login= "bank" """
            sql.execute(allironselected)
            alliron1 = sql.fetchall()
            alliron = alliron1[0][0]
            proveralliron += birshgold(alliron)
        if proveralliron > alliron:
            print('В банке не хватает золота')
            birsh()
        else:
            for i in range(kol):
                allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                sql.execute(allironselected)
                alliron1 = sql.fetchall()
                alliron = alliron1[0][0]
                birshgold(alliron)
                a += (1 * birshgold(alliron))
            print(f'Количества золота за {kol} алмазов: {a}')
            yesornoo = int(input('Согласны продолжитьть? (1/0)'))
            if yesornoo == 1:
                try:
                    sql.execute('BEGIN TRANSACTION')
                    for i in range(kol):
                        allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                        sql.execute(allironselected)
                        alliron1 = sql.fetchall()
                        alliron = alliron1[0][0]
                        birshgold(alliron)
                        sql_update_diamond = f"""UPDATE diamond set diamond = diamond-1 WHERE login = '{user_login}'"""
                        sql_update_airon = f"""UPDATE gold set gold = gold+(1*{birshgold(alliron)}) WHERE login = '{user_login}' """
                        sql_update_bankairon = f"""UPDATE gold set gold = gold-(1*{birshgold(alliron)}) WHERE login = "bank" """
                        sql.execute(sql_update_diamond)
                        sql.execute(sql_update_airon)
                        sql.execute(sql_update_bankairon)
                    db.commit()
                    db.commit()
                    db.commit()
                    db.commit()
                    print("Покупка завершенна")
                except sqlite3.Error as e:
                    print(e)
                    # Rollback the transaction in case of an error
                    print('except')
                    db.rollback()
                
                finally:
                    # Close the cursor and connection
                    birsh()
                            
            else:
                birsh()



def emerald():
    a = 0
    allironselected = """SELECT gold FROM gold WHERE login= "bank" """
    sql.execute(allironselected)
    alliron1 = sql.fetchall()
    alliron = alliron1[0][0]
    proveralliron = 0
    diamondselected = f"""SELECT diamond FROM diamond WHERE login='{user_login}'"""
    sql.execute(diamondselected)
    diamondi0 = sql.fetchall()
    diamondi1 = diamondi0[0][0]
    print('Вы выбрали изумруды')
    print(f'Сейчас у вас {diamondi1} алмазов')
    kol = int(input('Введите количество(в алмазах)'))
    if kol > diamondi1:
        print('У вас не хватает алмазов')
        birsh()
    else:
        for i in range(kol):
            allironselected = """SELECT gold FROM gold WHERE login= "bank" """
            sql.execute(allironselected)
            alliron1 = sql.fetchall()
            alliron = alliron1[0][0]
            proveralliron += birshemerald(alliron)
        if proveralliron > alliron:
            print('В банке не хватает изумрудов')
            birsh()
        else:
            for i in range(kol):
                allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                sql.execute(allironselected)
                alliron1 = sql.fetchall()
                alliron = alliron1[0][0]
                birshemerald(alliron)
                a += (1 * birshemerald(alliron))
            print(f'Количества изумрудов за {kol} алмазов: {a}')
            yesornoo = int(input('Согласны продолжитьть? (1/0)'))
            if yesornoo == 1:
                try:
                    sql.execute('BEGIN TRANSACTION')
                    for i in range(kol):
                        allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                        sql.execute(allironselected)
                        alliron1 = sql.fetchall()
                        alliron = alliron1[0][0]
                        birshemerald(alliron)
                        sql_update_diamond = f"""UPDATE diamond set diamond = diamond-1 WHERE login = '{user_login}'"""
                        sql_update_airon = f"""UPDATE gold set gold = gold+(1*{birshemerald(alliron)}) WHERE login = '{user_login}' """
                        sql_update_bankairon = f"""UPDATE gold set gold = gold-(1*{birshemerald(alliron)}) WHERE login = "bank" """
                        sql.execute(sql_update_diamond)
                        sql.execute(sql_update_airon)
                        sql.execute(sql_update_bankairon)
                    db.commit()
                    db.commit()
                    db.commit()
                    db.commit()
                    print("Покупка завершенна")
                except sqlite3.Error as e:
                    print(e)
                    # Rollback the transaction in case of an error
                    print('except')
                    db.rollback()
                
                finally:
                    # Close the cursor and connection
                    birsh()
                            
            else:
                birsh()

def quartz():
    a = 0
    allironselected = """SELECT gold FROM gold WHERE login= "bank" """
    sql.execute(allironselected)
    alliron1 = sql.fetchall()
    alliron = alliron1[0][0]
    proveralliron = 0
    diamondselected = f"""SELECT diamond FROM diamond WHERE login='{user_login}'"""
    sql.execute(diamondselected)
    diamondi0 = sql.fetchall()
    diamondi1 = diamondi0[0][0]
    print('Вы выбрали кварц')
    print(f'Сейчас у вас {diamondi1} алмазов')
    kol = int(input('Введите количество(в алмазах)'))
    if kol > diamondi1:
        print('У вас не хватает алмазов')
        birsh()
    else:
        for i in range(kol):
            allironselected = """SELECT gold FROM gold WHERE login= "bank" """
            sql.execute(allironselected)
            alliron1 = sql.fetchall()
            alliron = alliron1[0][0]
            proveralliron += birshquartz(alliron)
        if proveralliron > alliron:
            print('В банке не хватает кварца')
            birsh()
        else:
            for i in range(kol):
                allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                sql.execute(allironselected)
                alliron1 = sql.fetchall()
                alliron = alliron1[0][0]
                birshquartz(alliron)
                a += (1 * birshquartz(alliron))
            print(f'Количества кварца за {kol} алмазов: {a}')
            yesornoo = int(input('Согласны продолжитьть? (1/0)'))
            if yesornoo == 1:
                try:
                    sql.execute('BEGIN TRANSACTION')
                    for i in range(kol):
                        allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                        sql.execute(allironselected)
                        alliron1 = sql.fetchall()
                        alliron = alliron1[0][0]
                        birshquartz(alliron)
                        sql_update_diamond = f"""UPDATE diamond set diamond = diamond-1 WHERE login = '{user_login}'"""
                        sql_update_airon = f"""UPDATE gold set gold = gold+(1*{birshquartz(alliron)}) WHERE login = '{user_login}' """
                        sql_update_bankairon = f"""UPDATE gold set gold = gold-(1*{birshquartz(alliron)}) WHERE login = "bank" """
                        sql.execute(sql_update_diamond)
                        sql.execute(sql_update_airon)
                        sql.execute(sql_update_bankairon)
                    db.commit()
                    db.commit()
                    db.commit()
                    db.commit()
                    print("Покупка завершенна")
                except sqlite3.Error as e:
                    print(e)
                    # Rollback the transaction in case of an error
                    print('except')
                    db.rollback()
                
                finally:
                    # Close the cursor and connection
                    birsh()
                            
            else:
                birsh()

def nezerite():
    a = 0
    allironselected = """SELECT gold FROM gold WHERE login= "bank" """
    sql.execute(allironselected)
    alliron1 = sql.fetchall()
    alliron = alliron1[0][0]
    proveralliron = 0
    diamondselected = f"""SELECT diamond FROM diamond WHERE login='{user_login}'"""
    sql.execute(diamondselected)
    diamondi0 = sql.fetchall()
    diamondi1 = diamondi0[0][0]
    print('Вы выбрали незерит')
    print(f'Сейчас у вас {diamondi1} алмазов')
    kol = int(input('Введите количество(в алмазах)'))
    if kol > diamondi1:
        print('У вас не хватает алмазов')
        birsh()
    else:
        for i in range(kol):
            allironselected = """SELECT gold FROM gold WHERE login= "bank" """
            sql.execute(allironselected)
            alliron1 = sql.fetchall()
            alliron = alliron1[0][0]
            proveralliron += birshnezerite(alliron)
        if proveralliron > alliron:
            print('В банке не хватает незерита')
            birsh()
        else:
            for i in range(kol):
                allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                sql.execute(allironselected)
                alliron1 = sql.fetchall()
                alliron = alliron1[0][0]
                birshnezerite(alliron)
                a += (1 * birshnezerite(alliron))
            print(f'Количества незерита за {kol} алмазов: {a}')
            yesornoo = int(input('Согласны продолжитьть? (1/0)'))
            if yesornoo == 1:
                try:
                    sql.execute('BEGIN TRANSACTION')
                    for i in range(kol):
                        allironselected = """SELECT gold FROM gold WHERE login= "bank" """
                        sql.execute(allironselected)
                        alliron1 = sql.fetchall()
                        alliron = alliron1[0][0]
                        birshnezerite(alliron)
                        sql_update_diamond = f"""UPDATE diamond set diamond = diamond-1 WHERE login = '{user_login}'"""
                        sql_update_airon = f"""UPDATE gold set gold = gold+(1*{birshnezerite(alliron)}) WHERE login = '{user_login}' """
                        sql_update_bankairon = f"""UPDATE gold set gold = gold-(1*{birshnezerite(alliron)}) WHERE login = "bank" """
                        sql.execute(sql_update_diamond)
                        sql.execute(sql_update_airon)
                        sql.execute(sql_update_bankairon)
                    db.commit()
                    db.commit()
                    db.commit()
                    db.commit()
                    print("Покупка завершенна")
                except sqlite3.Error as e:
                    print(e)
                    # Rollback the transaction in case of an error
                    print('except')
                    db.rollback()
                
                finally:
                    # Close the cursor and connection
                    birsh()
                            
            else:
                birsh()

if __name__ == "__main__":
    main(False)
