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


