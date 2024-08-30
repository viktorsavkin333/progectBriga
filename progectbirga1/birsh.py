import sqlite3
from login import user_login 



db = sqlite3.connect('db.db')
sql = db.cursor()


user_login = 2183

def birsh():
    num1 = int(input('Введите что вы хотите купить от 1 до 5 где: \n 1 - железо \n 2 - золото \n 3 - изумруд \n 4 - кварц \n 5 - незерит \n (0 для выхода): '))
    if num1 == 1:
        sell_resourse('iron', user_login)
    elif num1 == 2:
        sell_resourse('gold', user_login)
    elif num1 == 3:
        sell_resourse('emerald', user_login)
    elif num1 == 4:
        sell_resourse('quartz', user_login)
    elif num1 == 5:
        sell_resourse('nezerite', user_login)
    else:
        return True
        #print(balance)
    

# переделать функцию под каждый ресурс ресурс

resourse = 'iron'

def sell_resourse(resourse, user_login):
    proveralliron = 0
    if resourse == 'iron':
        resourse_name = 'желез'
        user_choise = 1
    elif resourse == 'gold':
        resourse_name = 'золот'
        user_choise = 2
    elif resourse == 'emerald':
        resourse_name = 'изумруд'
        user_choise = 3
    elif resourse == 'quartz':
        resourse_name = 'кварц'
        user_choise = 4
    elif resourse == 'nezerite':
        resourse_name = 'незерит'
        user_choise = 5
    calculators = [birshiron, birshgold, birshemerald, birshquartz, birshnezerite]
    a = 0
    prise = calculators[user_choise-1]
    allironselected = f"""SELECT {resourse} FROM {resourse} WHERE login= "bank" """
    sql.execute(allironselected)
    alliron1 = sql.fetchall()
    alliron = alliron1[0][0]
    diamondselected = f"""SELECT diamond FROM diamond WHERE login='{user_login}'"""
    sql.execute(diamondselected)
    diamondi0 = sql.fetchall()
    diamondi1 = diamondi0[0][0]
    print(f'Вы выбрали {resourse_name}о')
    print(f'Сейчас у вас {diamondi1} алмазов')
    kol = int(input('Введите количество(в алмазах)'))
    if kol > diamondi1:
        print('У вас не хватает алмазов')
        birsh()
    else:
        for i in range(kol):
            allironselected = f"""SELECT gold FROM gold WHERE login= "bank" """
            sql.execute(allironselected)
            alliron1 = sql.fetchall()
            alliron = alliron1[0][0]
            proveralliron += prise(alliron)
        if proveralliron > alliron:
            print('В банке не хватает {resourse_name}а')
            birsh()
        else:
            for i in range(kol):
                allironselected = f"""SELECT {resourse} FROM {resourse} WHERE login= "bank" """
                sql.execute(allironselected)
                alliron1 = sql.fetchall()
                alliron = alliron1[0][0]
                prise(alliron)
                a += (1 * prise(alliron))
            print(f'Количества {resourse_name}а за {kol} алмазов: {a}')
            yesornoo = int(input('Согласны продолжитьть? (1/0)'))
            if yesornoo == 1:
                try:
                    sql.execute('BEGIN TRANSACTION')
                    for i in range(kol):
                        allironselected = f"""SELECT {resourse} FROM {resourse} WHERE login= "bank" """
                        sql.execute(allironselected)
                        alliron1 = sql.fetchall()
                        alliron = alliron1[0][0]
                        prise(alliron)
                        sql_update_diamond = f"""UPDATE diamond set diamond = diamond-1 WHERE login = '{user_login}'"""
                        sql_update_airon = f"""UPDATE {resourse} set {resourse} = {resourse}+(1*{prise(alliron)}) WHERE login = '{user_login}' """
                        sql_update_bankairon = f"""UPDATE {resourse} set {resourse} = {resourse}-(1*{prise(alliron)}) WHERE login = "bank" """
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
                    return None
                            
            else:
                return None


priseiron = 0

def birshiron(alliron):
    priseiron = 0
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
    priseiron = 0
    if alliron <= 50:
        priseiron = 0.5
    elif 500 >= alliron >= 51:
        priseiron = 2.5
    elif 2500 >= alliron >= 501:
        priseiron = 5
    elif 10000 >= alliron >= 2501:
        priseiron = 10
    elif 50000 >= alliron >= 10001:
        priseiron = 20
    return priseiron

def birshemerald(alliron):
    priseiron = 0
    if alliron <= 50:
        priseiron = 0.3
    elif 500 >= alliron >= 51:
        priseiron = 1.6
    elif 2500 >= alliron >= 501:
        priseiron = 3
    elif 10000 >= alliron >= 2501:
        priseiron = 6
    elif 50000 >= alliron >= 10001:
        priseiron = 12
    return priseiron

def birshquartz(alliron):
    priseiron = 0
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
    priseiron = 0
    if alliron <= 50:
        priseiron = 0.3
    elif 500 >= alliron >= 51:
        priseiron = 1.6
    elif 2500 >= alliron >= 501:
        priseiron = 3
    elif 10000 >= alliron >= 2501:
        priseiron = 6
    elif 50000 >= alliron >= 10001:
        priseiron = 12
    return priseiron

if __name__ == "__main__":
    birsh()
    main(False)
