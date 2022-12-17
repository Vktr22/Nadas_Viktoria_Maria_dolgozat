import random



def beker():
    paros = int(input('Kérek egy páros számot! '))
    while paros % 2 != 0:
        paros = int(input('Ez nem páros! PÁROS számot kérek! '))


def beker2(i):
    paros = int(input(f"Kérem az {i}. páros számot! "))
    while paros % 2 != 0:
        paros = int(input(f'Ez nem PÁROS! Kérem az {i}. páros számot! '))
    return paros

def harom_bekeros():
    lista = []
    i = 0
    while i < 3:
        lista.append(beker2(i + 1))
        i += 1
    legkisebb(lista)

def legkisebb(lista):

    if lista[0] <= lista[1]:
        if lista[0] <= lista[2]:
            index = 0
        else:
            index = 2
    else:
        if lista[1] <= lista[2]:
            index = 1
        else:
            index = 2
    print(f'{index + 1}. lépésben adta meg a legkisebb páros számot, melynek értéke: {lista[index]}')

# Második feladat

def random_fgv():
    lista = []
    i = 0
    while i < 13:
        random_ertek = random.randint(-40, 150)
        i += 1
        lista.append(random_ertek)
    print(lista)
    return lista

def ketjegyuek_szama(lista):

    i = 0
    szamolo = 0
    while i < 13:
        if (lista[i] < -9) or (lista[i] > 9) and (lista[i] < 100):
            szamolo += 1
        i += 1
    print(f'A kétjegyű számok száma: {szamolo}')
    return szamolo

def paros_osszege(lista):

    i = 0
    osszeg = 0
    while i < 13:
        if lista[i] % 2 == 0:
            osszeg += lista[i]
        i += 1
    return osszeg

def paratlan_osszege(lista):

    i = 0
    osszeg = 0
    while i < 13:
        if lista[i] % 2 != 0:
            osszeg += lista[i]
        i += 1
    return osszeg

def melyik_nagyobb(paros, paratlan):
    if paros > paratlan:
        print(f"A párosok összege volt a nagyobb. A párosok összege {paros} > a páratlanok összege {paratlan}")
    elif paros == paratlan:
        print("A páros számok összege megegyezik a páratlanok összegével.")
    else:
        print(f"A páratlanok összege volt a nagyobb. A párosok összege {paros} < a páratlanok összege {paratlan}")

# harmadik feladat
def stadion(fajl):
    stadionok = open(fajl,"r", encoding='utf-8')
    sorok = stadionok.readlines()
    sorlista = feldolgozas(sorok)
    csapatok_db(sorlista)
    new_york_csapatok(sorlista)
def feldolgozas(sorok):
    i = 1
    sorlista = []
    while i < len(sorok):
        egy_sor = sorok[i].strip().split(';')
        sorlista.append(egy_sor)
        i += 1
    print(sorlista)
    return sorlista
def csapatok_db(lista):

    i = 0
    csapatszam = 0
    while i < len(lista):
        stadionlista = lista[i]
        csapatszam += int(stadionlista[2])
        i += 1
    print(csapatszam)

def new_york_csapatok(lista):

    i = 0
    while i < len(lista):
        stadionlista = lista[i]
        if stadionlista[1] == "New York":
            print(f'Stadion neve: {stadionlista[0]}, csapatok szama: {stadionlista[2]}.')
        i += 1