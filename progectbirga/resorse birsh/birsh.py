a = 0
balance = {'алмазы': 10000,
           'железо': 0}

alliron = 10000

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



while balance['алмазы'] >= 0:
    num1 = int(input('Введите что вы хотите купить от 1 до 5: '))
    if num1 == 1:
        diamondi1 = balance['алмазы']
        print('Вы выбрали железо')
        print(f'Сейчас у вас {diamondi1} алмазов')
        kol = int(input('Введите количество(в алмазах)'))
        if kol > balance['алмазы']:
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
                    alliron -= 1
            else:
                continue
            print(alliron)
        print(balance)

# посмотреть ка опдключяеться SQLITE PYTHON ок?
# школьные конференции, олимпиады по програмированию
# flask