def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  res=0
  for elem in compareDates:
    if (jour1,mois1,annee1<jour2,mois2,annee2):
      res=-1
    elif (jour1,mois1,annee1==jour2,mois2,annee2):
      res=0
    else:
      res=1
  return res