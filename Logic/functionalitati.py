from Domain.librarie import getTipReducere, creeazaVanzare, getId, getTitlucarte, getGencarte, getPret
from Logic.CRUD import modificaVanzare


def discountptrreducere(lista):
    '''
    aplica un discount de 5% pentru reducerile de tip silver si o reducere de 10% ptr cele gold
    :param lista: lista cartilor
    :return: lista continand cartile cu modificarile cerute
    '''
    listanoua = []
    for vanzare in lista:
        if getTipReducere(vanzare) == "silver":
            vanzarenoua = creeazaVanzare (getId(vanzare),
                                         getTitlucarte(vanzare),
                                         getGencarte(vanzare),
                                         getPret(vanzare) - getPret(vanzare) * 0.05,
                                         getTipReducere(vanzare),
                                         )

            listanoua.append(vanzarenoua)
        elif getTipReducere(vanzare) == "gold":
            cartenoua = creeazaVanzare( getId(vanzare),
            getTitlucarte(vanzare),
            getGencarte(vanzare),
            getPret(vanzare) - getPret(vanzare) * 0.1,
            getTipReducere(vanzare),
            )
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)

    return listanoua

def modificaGenulCartii(gencarte, titlu, lista):
        lnoua = []
        for vanzare in lista:
            if getTitlucarte(vanzare) == titlu:

                listanoua = creeazaVanzare(getId(vanzare),
                                             getTitlucarte(vanzare),
                                             gencarte,
                                             getPret(vanzare),
                                             getTipReducere(vanzare),
                                             )
                lnoua.append(listanoua)
            else:
                lnoua.append(vanzare)
        return lnoua