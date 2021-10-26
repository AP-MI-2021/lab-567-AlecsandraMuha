from Tests.testCRUD import testAdaugaVanzare, testStergeVanzare, testModificaVanzare
from Tests.testDomain import testVanzare
from Tests.testfunctionalitati import testModificareGen, testdiscountptrreducere


def runAllTests():
    testVanzare()
    testAdaugaVanzare()
    testModificareGen()
    testdiscountptrreducere()
    testStergeVanzare()
    testModificaVanzare()