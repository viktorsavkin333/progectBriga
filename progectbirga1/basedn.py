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
    db.commit()
    if sql.fetchone() is None:
        print("Такого пользователя не существует")
        main(False)
    else:
        registred = True
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
                main(False)
        if registred == True:
            help = "Список команд: /help - Команды, /user - Профиль, /birsh - Перейти на биржу"
            print(help)
            enter = input("Введите команду: ")
            if enter == '/help':
                print(help)
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
    allselect = f"""SELECT * FROM users WHERE login={user_login}"""
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
    print(allironselected)
    proveralliron = 0
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
                proveralliron += priseiron
            if proveralliron > alliron:
                print('В банке не хватает железа')
                birsh()
            else:
                for i in range(kol):
                    allironselected = """SELECT airon FROM users WHERE login= "bank" """
                    sql.execute(allironselected)
                    alliron1 = sql.fetchall()
                    alliron = alliron1[0][0]
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
                    a += (1 * priseiron)
                print(f'Количества железа за {kol} алмазов: {a}')
                yesornoo = int(input('Согласны продолжитьть? (1/0)'))
                if yesornoo == 1:
                    for i in range(kol):
                        allironselected = """SELECT airon FROM users WHERE login= "bank" """
                        sql.execute(allironselected)
                        alliron1 = sql.fetchall()
                        alliron = alliron1[0][0]
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
                        #sql_update_diamond = f"""UPDATE users set diamond = diamond-1 WHERE login = {user_login}"""
                        sql_update_airon = f"""UPDATE users set airon = airon+(1*{priseiron}) WHERE login = {user_login} """
                        #sql.execute(sql_update_diamond)
                        sql.execute(sql_update_airon)
                        db.commit
                    db.commit
                    birsh()
                else:
                    birsh()
    else:
        return
        #print(balance)












main(False)


