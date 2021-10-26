from Domain.librarie import getGencarte
from Logic.CRUD import adaugaVanzare, getById
from Logic.functionalitati import modificaGenulCartii


def testModificareGen():
    lista = []
    lista = adaugaVanzare("1", "Enigma Otiliei", "Roman realist", 12, "Gold", lista)
    lista = adaugaVanzare("2", "Harap-Alb", "basm", 15, "None", lista)
    lista = adaugaVanzare("3", "Moara cu noroc", "Nuvela", 30, "Gold", lista)


    lista = modificaGenulCartii("basm cult","Harap-Alb",lista)

    assert getGencarte(getById("1", lista)) == "Roman realist"
    assert getGencarte(getById("2", lista)) == "basm cult"
    assert getGencarte(getById("3", lista)) == "Nuvela"