def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  if jour1<jour2 or mois1<mois2 or annee1<annee2:
    res=-1
    if jour1==jour2 or mois==mois2 or annee1==annee2:
      res=0
  else:
    res=1
  return res