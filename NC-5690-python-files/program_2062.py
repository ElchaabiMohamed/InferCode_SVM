def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
    d1=jour1,mois1,annee1
    d2=jour2,mois2,annee2
    if d1>d2:
      res=-1
    elif d2>d1:
      res=1
    else:
      res=0
    return res