import sqlite3
from login import user_login 

db = sqlite3.connect('db.db')
sql = db.cursor()



def user():
    select_diamond_login = f"""SELECT * FROM diamond WHERE login = '{user_login}' """
    sql.execute(select_diamond_login)
    login_diamond = sql.fetchall()
    print('Ваш логин: ', login_diamond[0][0])
    print('Ваше кол-во алмазов: ', login_diamond[0][1])

    selectiron = f"""SELECT iron FROM iron WHERE login = '{user_login}' """
    sql.execute(selectiron)
    iron = sql.fetchall()
    print('Ваше кол-во железа: ', iron[0][0])

    selectgold = f"""SELECT gold FROM gold WHERE login = '{user_login}' """
    sql.execute(selectgold)
    gold = sql.fetchall()
    print('Ваше кол-во золота: ', gold[0][0])

    selectemerald = f"""SELECT emerald FROM emerald WHERE login = '{user_login}' """
    sql.execute(selectemerald)
    emerald = sql.fetchall()
    print('Ваше кол-во изумрудов: ', emerald[0][0])

    selectquartz = f"""SELECT quartz FROM quartz WHERE login = '{user_login}' """
    sql.execute(selectquartz)
    quartz = sql.fetchall()
    print('Ваше кол-во кварца: ', quartz[0][0])

    selectnezerite = f"""SELECT quartz FROM quartz WHERE login = '{user_login}' """
    sql.execute(selectnezerite)
    nezerite = sql.fetchall()
    print('Ваше кол-во незерита: ', nezerite[0][0])


