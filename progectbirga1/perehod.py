a = 0
balance = {'алмазы': 10000,
           'железо': 0}

allironselected = """SELECT airon FROM users WHERE login=bank"""
sql.execute(allironselected)
alliron = sql.fetchall()

diamondi1 = f"""UPDATE users set diamond = diamond+1 WHERE login = {user_login}"""
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

diamondselect = f"""SELECT * FROM users WHERE login={user_login}"""
sql.execute(diamondselect)
diamond = sql.fetchall()


def birsh():
    allironselected = """SELECT airon FROM users WHERE login=bank"""
    sql.execute(allironselected)
    alliron = sql.fetchall()
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
    num1 = int(input('Введите что вы хотите купить от 1 до 1: '))
    if num1 == 1:
        diamondi1 = """SELECT diamond FROM users WHERE login=bank"""
        sql.execute(allironselected)
        alliron = sql.fetchall()
        print('Вы выбрали железо')
        print(f'Сейчас у вас {diamondi1} алмазов')
        kol = int(input('Введите количество(в алмазах)'))
        if kol > diamondi1:
            print('У вас не хватает алмазов')
        else:
            for i in range(kol):
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
            else:
                for i in range(kol):
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
                        balance['алмазы'] -= 1
                        balance['железо'] += 1 * priseiron
                        alliron -= priseiron
                else:
                    continue
            print(alliron)
        print(balance)



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
