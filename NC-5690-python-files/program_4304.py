def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
    if jours1==jours2 and mois1==mois2 and annee1==annee2:
      res=0
    elif jours1<jours2 or mois1<mois2 or annee1<annee2:
         res=-1
    else:
      res=1
    return res