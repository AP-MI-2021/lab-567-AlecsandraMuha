from Domain.librarie import toString, getTitlucarte, getPret, getId, getTipReducere
from Logic.CRUD import stergeVanzare, adaugaVanzare, modificaVanzare
from Logic.functionalitati import discountptrreducere, modificaGenulCartii


def printMenu():
    print("1.Adauga vanzare")
    print("2.Sterge vanzare")
    print("3.Modifica vanzare")
    print("4.Aplica discount pentru reducerile de tip silver/gold")
    print("5.Modifica genul pentru un titlu dat.")
    print("a.Afiseza lista de vanzari")
    print("x.Iesire")

def uiAdaugaVanzare(lista):
    id =(input("Da-ti id-ul: "))
    titlucarte = input("Dati numele cartii: ")
    gencarte = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii:"))
    tipreducere = input("Dati tipul reducerii: ")
    return adaugaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)

def uiStergeVanzare(lista):
    id = (input("Dati id-ul unei vanzari care ar trebui sa fie stearsa: "))
    return stergeVanzare(id, lista)
def uiModificaVanzare(lista):
    id = (input("Da-ti id-ul: "))
    titlucarte = input("Dati noul nume al cartii: ")
    gencarte = input("Dati noul gen al cartii: ")
    pret = float(input("Dati noul pret al cartii:"))
    tipreducere = input("Dati noul tip de reducere: ")
    return modificaVanzare(id, titlucarte, gencarte, pret, tipreducere,lista)
def uiDiscountVanzare(lista):
    return discountptrreducere(lista)
def uiModificaregen(lista):
    titlu = input("Dati titlul cartii: ")
    gencarte= input("Dati noul gen al cartii: ")
    return  modificaGenulCartii(gencarte,titlu,lista)
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
            lista = uiModificaregen(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")
