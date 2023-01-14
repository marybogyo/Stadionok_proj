from Stadion import Stadion

stadionok_lista = []
def fajl_beolvasa():
    fajlom = open("stadionok.txt", "r", encoding= "utf-8")
    '''fejlec beolvasása'''
    fajlom.readline()
    '''fajl tartalmának a beolvaása'''
    fajl_tartalom = fajlom.readlines()
    print(fajl_tartalom)
    '''fajl lezárása'''
    fajlom.close()
    feldolgoz(fajl_tartalom)

def feldolgoz(faj_tartalom):
    '''fajl tartalom egy lista, az egyes elemeit kell szétválasztani, pontos veszző szerint'''

    i = 0
    while i < len(faj_tartalom):
        """soronként történik a feldolgozás""" '''strip leveszi a \n jelet'''
        sor = faj_tartalom[i].strip().split(";")
        #print(sor)
        '''példányosítjuk az osztályunkat, létrehozzuk a konkrét objektumot = osztály példányt'''
        stadion = Stadion(sor)
        #print(stadion)
        stadionok_lista.append(stadion)
        i += 1
    #print(stadionok_lista[3].stadion_nev)
    print(stadionok_lista)

def nevyorki_stadionok_szama():
    i = 0
    stadionszam = 0
    while i < len(stadionok_lista):
        if stadionok_lista[i].varos == "New York":
            stadionszam += 1
        i += 1
    return stadionszam

def osszescsapatszam():
    i = 0
    csapatosszeg = 0
    while i < len(stadionok_lista):
        csapatosszeg += stadionok_lista[i].csapatszam

        i += 1
    return csapatosszeg

def stadionok1900elott():
    i = 0

    #print(int(ev[0]))
    while i < len(stadionok_lista):
        ev = stadionok_lista[i].elso.split("-")
        if (int(ev[0]) < 1900):
            print(stadionok_lista[i].stadion_nev)
        i += 1

def ketszaz():
    i = 0
    stadiondb = 0
    while i < len(stadionok_lista):
        ev = stadionok_lista[i].utolso.split("-")
        if (int(ev[0]) >= 200):
            stadiondb += stadionok_lista[i].csapatszam
        i += 1
    return stadiondb

def merkozes_buffalo():
    i = 0
    buff_merk = 0
    while i < len(stadionok_lista):
        if (stadionok_lista[i].varos == "Buffalo"):
            buff_merk += 1
        i += 1
    return buff_merk