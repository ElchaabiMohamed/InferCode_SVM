def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  if annee1<annee2:
    res=-1
  elif jour1==None or mois1==None or annee1==None or jour2==None or mois2==None or annee2==None:
    res=None
  elif jour1==jour2 and mois1==mois2 and annee1==annee2:
      res=0
  else:
    res=1
  return res