import sqlite3
from reg import reg
from setup import cozdanie_bd
from login import login


db = sqlite3.connect('db.db')
sql = db.cursor()



def main(registred):
    if registred == False:
        help = "Список команд: /leave - Выход, /new_user - Регистрация, /login - Вход"
        print(help)
        enter = input("Введите команду: ")
        if enter == '/leave':
            print()
        elif enter == '/new_user':
            reg(False)
            main(False)
        elif enter == '/login':
            is_logined = login()
            main(is_logined)
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
            from user_profile import user
            user()
            main(True)
        elif enter == '/birsh':
            from birsh import birsh
            birsh()
            main(True)
        else:
            print('Неверная команда')
            main(True)


if __name__ == "__main__":
    main(False)