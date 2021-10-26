from Tests.testCRUD import testAdaugaVanzare
from Tests.testDomain import testVanzare
from Tests.testfunctionalitati import testModificareGen


def runAllTests():
    testVanzare()
    testAdaugaVanzare()
    testModificareGen()