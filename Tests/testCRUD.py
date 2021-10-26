from Domain.librarie import getId, getTitlucarte, getGencarte, getPret, getTipReducere
from Logic.CRUD import adaugaVanzare, getById, stergeVanzare, modificaVanzare


def testAdaugaVanzare():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 15, "None",lista)
    assert getId(getById("1",lista)) == "1"
    assert getTitlucarte(getById("1",lista)) == "Harap-Alb"
    assert getGencarte(getById("1",lista)) == "Basm"
    assert getPret(getById("1",lista)) == 15
    assert getTipReducere(getById("1",lista)) == "None"

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
def testModificaVanzare():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 15, "None",lista)
    lista = adaugaVanzare("2", "Ion", "Roman", 10, "None", lista)
    lista = modificaVanzare("2", "Ion", "Roman realist", 10, "Gold", lista)
    assert len(lista) == 2
    assert getId(getById("2", lista)) == "2"
    assert getTitlucarte(getById("2", lista)) == "Ion"
    assert getGencarte(getById("1", lista)) == "Roman realist"
    assert getPret(getById("1", lista)) == 10
    assert getTipReducere(getById("1", lista)) == "Gold"