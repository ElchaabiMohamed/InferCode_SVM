def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  res=''
  if annee1==annee2 and mois1==mois2 and jour1==jour2:
    res=0
  if annee1<annee2:
    res=-1
  elif annee1>annee2:
      res=1
  if annee1==annee2 and mois1<mois2:
    res=-1
  elif annee1==annee2 and mois1>mois2:
      res=1
  if annee1==annee2 and mois1==mois2 and jour1<jour2:
    res=-1
  elif annee1==annee2 and mois1==mois2 and jour1>jour2:
      res=1
  return res