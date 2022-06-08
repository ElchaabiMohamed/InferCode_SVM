def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  if annee1<annee2:
    res=-1
  elif date1==None or date2==None:
    Date=jour,mois,annee
    res=None
  elif jour1==jour2 and mois1==mois2 and annee1==annee2:
      res=0
  else:
    res=1
  return res