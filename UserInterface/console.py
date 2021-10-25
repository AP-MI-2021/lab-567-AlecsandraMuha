from Domain.librarie import toString
from Logic.CRUD import stergeVanzare, adaugaVanzare, modificaVanzare


def printMenu():
    print("1.Adauga vanzare")
    print("2.Sterge vanzare")
    print("3.Modifica vanzare")
    print("a.Afiseza lista de vanzari")
    print("x.Iesire")

def uiAdaugaVanzare(lista):
    id = input("Da-ti id-ul: ")
    titlucarte = input("Dati numele cartii: ")
    gencarte = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii:"))
    tipreducere = input("Dati tipul reducerii: ")
    return adaugaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)

def uiStergeVanzare(lista):
    id = input("Dati id-ul unei vanzari care ar trebui sa fie stearsa: ")
    return stergeVanzare(id, lista)
def uiModificaVanzare(lista):
    id = input("Da-ti id-ul: ")
    titlucarte = input("Dati numele cartii: ")
    gencarte = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii:"))
    tipreducere = input("Dati tipul reducerii: ")
    return modificaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)
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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")
