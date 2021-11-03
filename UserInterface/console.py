from Domain.librarie import toString, getTitlucarte, getPret, getId, getTipReducere
from Logic.CRUD import stergeVanzare, adaugaVanzare, modificaVanzare
from Logic.functionalitati import discountptrreducere, modificaGenulCartii, pretminim, ordonareDupaPret


def printMenu():
    print("1.Adauga vanzare")
    print("2.Sterge vanzare")
    print("3.Modifica vanzare")
    print("4.Aplica discount pentru reducerile de tip silver/gold")
    print("5.Modifica genul pentru un titlu dat.")
    print("6.Determinarea prețului minim pentru fiecare gen")
    print("7.Ordonarea vânzărilor crescător după preț")
    print("a.Afiseza lista de vanzari")
    print("x.Iesire")

def uiAdaugaVanzare(lista):
    try:
        id =int(input("Da-ti id-ul: "))
        titlucarte = input("Dati numele cartii: ")
        gencarte = input("Dati genul cartii: ")
        pret = float(input("Dati pretul cartii:"))
        tipreducere = input("Dati tipul reducerii none/silver/gold: ")
        return adaugaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeVanzare(lista):
    try:
        id = int(input("Dati id-ul unei vanzari care ar trebui sa fie stearsa: "))
        return stergeVanzare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiModificaVanzare(lista):
    try:
        id = int(input("Da-ti id-ul: "))
        titlucarte = input("Dati noul nume al cartii: ")
        gencarte = input("Dati noul gen al cartii: ")
        pret = float(input("Dati noul pret al cartii:"))
        tipreducere = input("Dati noul tip de reducere none/silver/gold: ")
        return modificaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiDiscountVanzare(lista):
    return discountptrreducere(lista)
def uiModificaregen(lista):
    try:
        titlu = input("Dati titlul cartii: ")
        gencarte= input("Dati noul gen al cartii: ")
        return  modificaGenulCartii(gencarte,titlu,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiPretMinim(lista):
    rezultat = pretminim(lista)
    for gen in rezultat:
        print("Genul {} are pretul minim {}".format(gen, rezultat[gen]))
def uiOrdonareDupaPret(lista):

    showAll(ordonareDupaPret(lista))

def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaVanzare(lista)
        elif optiune == "2":
            lista = uiStergeVanzare(lista)
        elif optiune == "3":
            lista = uiModificaVanzare(lista)
        elif optiune == "4":
            lista = uiDiscountVanzare(lista)
        elif optiune == "5":
            uiModificaregen(lista)
        elif optiune == "6":
            uiPretMinim(lista)
        elif optiune == "7":
            uiOrdonareDupaPret(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")
