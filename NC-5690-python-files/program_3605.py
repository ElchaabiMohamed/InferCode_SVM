import datetime


def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
    frist_date = datetime.datetime(annee1,mois1,jour1)
    second_date = datetime.datetime(annee2,mois2,jour2)
    res = 0
    if frist_date < second_date:
        res = -1
    elif frist_date > second_date:
        res = 1

    return res
    