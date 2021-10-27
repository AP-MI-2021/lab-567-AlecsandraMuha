def creeazaVanzare(id, titlucarte, gencarte, pret, tipreducere):
    '''
    creeaza o vanzare dintr-o librarie
    :param id: string
    :param titlucarte: string
    :param gencarte: string
    :param pret: float
    :param tipreducere: string
    :return: un dictionar ce retine o vanzare a unei librarii
    '''
    vanzare = [id, titlucarte, gencarte, pret, tipreducere]
    return vanzare
def getId(vanzare):
    '''
    ia id-ul unei vanzari
    :param vanzare: dictionar de tipul vanzare
    :return: id-ul vanzarii
    '''
    return vanzare[0]

def getTitlucarte(vanzare):
    '''
    ia titlul unei carti
    :param vanzare: dictionar de tipul vanzare
    :return: titlul unei carti
    '''
    return vanzare[1]

def getGencarte(vanzare):
    return vanzare[2]

def getPret(vanzare):
    return vanzare[3]

def getTipReducere(vanzare):
    return vanzare[4]
def toString(vanzare):
    return "id: {}, titlu carte: {}, gen carte: {}, pret: {}, tip reducere: {}".format(
        getId(vanzare),
        getTitlucarte(vanzare),
        getGencarte(vanzare),
        getPret(vanzare),
        getTipReducere(vanzare)
    )
