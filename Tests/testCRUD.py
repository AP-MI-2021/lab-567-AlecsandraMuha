from Domain.librarie import getId, getTitlucarte, getGencarte, getPret, getTipReducere
from Logic.CRUD import adaugaVanzare, getById


def testAdaugaVanzare():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 15, "None",lista)
    assert getId(getById("1",lista)) == "1"
    assert getTitlucarte(("1",lista)) == "Harap-Alb"
    assert getGencarte(("1",lista)) == "Basm"
    assert getPret(("1",lista)) == 15
    assert getTipReducere(("1",lista)) == "None"

def testStergeVanzare():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 15, "None",lista)
    lista = adaugaVanzare("2", "Ion", "Roman", 10, "None", lista)
    lista = stergeVanzare("1",lista)
    assert len(lista) == 1
    assert getById("1", lista) is None

    lista = stergeVanzare("3",lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None