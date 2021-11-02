from Domain.librarie import creeazaVanzare
from Logic.CRUD import adaugaVanzare
from Tests.testALL import runAllTests
from UserInterface.console import runMenu




def main():
    runAllTests()
    lista = []
    lista = adaugaVanzare(1, "Harap-Alb", "Basm", 15.0, "None",lista)
    lista = adaugaVanzare(2, "Ion", "Roman", 10.0, "None", lista)
    runMenu(lista)
if __name__ == '__main__':
    main()