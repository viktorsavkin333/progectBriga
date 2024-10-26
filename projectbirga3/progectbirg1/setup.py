import sqlite3

db = sqlite3.connect('db.db')
sql = db.cursor()



# Уберите кавычки один раз после того как создали бд чтобы добавить аккаунт банка
def create_bank_account():
    setup1 = sql.execute(f"SELECT login FROM users WHERE login = 'bank' AND password = 'bank'")
    setup2 = sql.fetchall()
    if setup2 ==  []:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?) ", ('bank', 'bank', 'bank'))
        sql.execute(f"INSERT INTO diamond VALUES (?, ?)", ('bank', 0))
        sql.execute(f"INSERT INTO iron VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO gold VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO emerald VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO quartz VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO nezerite VALUES (?, ?)", ('bank', 10000)) 
        db.commit()
        db.commit()
        db.commit()
        db.commit()
        db.commit()
        db.commit()
        print(2)
        return
    else:
        print(3)
        return


def cozdanie_bd():
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
    print(1)
    create_bank_account()