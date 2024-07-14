import sqlite3

global enter 
help = "Command List: /help - Show full list of commands, /new_user - Create new user, /login - Login to user"

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
    user_login = input("Enter login: ")
    user_password = input("Enter password: ")
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("This user does not exist")
        main()
    else:
        sql_update_query = f"""Update users set diamond = diamond-1  where login = {user_login}"""
        sql.execute(sql_update_query)
        db.commit()
        print("Запись успешно обновлена")
        sql.close()

def reg():
    user_login = input("Enter login: ")
    user_password = input("Enter password: ")
    diamond = 100
    airon = 0
    abc(user_login, user_password, diamond, airon)

def main():
        print(help)
        enter = input("Enter the command: ")
        if enter == '/help':
            print(help)
        elif enter == '/new_user':
            reg()
        elif enter == '/login':
            login()

def abc (user_login, user_password, diamond, airon):
        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (user_login, user_password, diamond, airon))
            db.commit()
            print('You have successfully registered')
            main()
        else:
            print('Such a record already exists')
            main()

main()