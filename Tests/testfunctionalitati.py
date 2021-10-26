from Domain.librarie import getGencarte, getTipReducere, getPret
from Logic.CRUD import adaugaVanzare, getById
from Logic.functionalitati import modificaGenulCartii, discountptrreducere


def testdiscountptrreducere():
    lista = []
    lista = adaugaVanzare("1", "Enigma Otiliei", "Roman realist", 20.0, "gold", lista)
    lista = adaugaVanzare("2", "Harap-Alb", "basm", 15.0, "none", lista)
    lista = adaugaVanzare("3", "Moara cu noroc", "Nuvela", 30.0, "gold", lista)
    lista = discountptrreducere(lista)
    assert getPret(lista[0]) == 18.0
    assert getPret(lista[1]) == 15.0
    assert getPret(lista[2]) == 27.0
def testModificareGen():

    lista = []
    lista = adaugaVanzare("1", "Enigma Otiliei", "Roman realist", 12, "Gold", lista)
    lista = adaugaVanzare("2", "Harap-Alb", "basm", 15, "None", lista)
    lista = adaugaVanzare("3", "Moara cu noroc", "Nuvela", 30, "Gold", lista)

    lista = modificaGenulCartii("basm cult", "Harap-Alb", lista)

    assert getGencarte(getById("1", lista)) == "Roman realist"
    assert getGencarte(getById("2", lista)) == "basm cult"
    assert getGencarte(getById("3", lista)) == "Nuvela"