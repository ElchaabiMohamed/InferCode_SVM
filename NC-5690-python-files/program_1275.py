def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
    if annee1<annee2 :
        res=-1
    elif annee1>annee2 :
        res=1
    elif mois1<mois2:
        res=-1
    elif mois1>mois2:
        res=1
    elif jour1<jour2:
        res=-1
    elif jour1>jour2:
        res=1
    else: #annee1=annee2 et mois1=mois2 et jour1=jour2
        res=0
    return res