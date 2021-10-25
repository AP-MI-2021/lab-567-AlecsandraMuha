from Domain.librarie import getId, creeazaVanzare


def adaugaVanzare(id, titlucarte, gencarte, pret, tipreducere, lista):
    '''
    adauga o vanzare noua in lista
    :param id: id carte, string
    :param titlucarte: titlul cartii, string
    :param gencarte: genul cartii , string
    :param pret: pretul cartii, float
    :param tipreducere: tipul reducerii, string
    :param lista: lista de vanzari de carti
    :return: lista noua, modificata
    '''
    vanzare = creeazaVanzare(id, titlucarte, gencarte, pret, tipreducere)
    return lista + [vanzare]

def stergeVanzare(id, lista):
    '''
    sterge o vanzare din lista
    :param id: id carte, string
    :param titlucarte: titlul cartii, string
    :param gencarte: genul cartii , string
    :param pret: pretul cartii, float
    :param tipreducere: tipul reducerii, string
    :param lista: lista de vanzari de carti
    :return: lista noua, modificata
    '''

    return [vanzare for vanzare in lista if getId(vanzare) != id]
def modificaVanzare(id, titlucarte, gencarte, pret, tipreducere, lista):
    '''

    :param id:
    :param titlucarte:
    :param gencarte:
    :param pret:
    :param tipreducere:
    :param lista:
    :return:
    '''
    listanoua = []
    if vanzare in lista:
        if getId(vanzare) == id:
            vanzareNoua == creeazaVanzare(id, titlucarte, gencarte, pret, tipreducere)
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)
    return listanoua
def getById(id,lista):
    '''

    :param id:
    :param lista:
    :return:
    '''
    for vanzare in lista:
        if getId(vanzare) == id:
            return vanzare
    return None

