from Tests.testCRUD import testAdaugaVanzare
from Tests.testDomain import testVanzare


def runAllTests():
    testVanzare()
    testAdaugaVanzare()