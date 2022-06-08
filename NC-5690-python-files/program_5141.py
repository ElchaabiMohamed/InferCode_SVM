def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  res=None
  if jour1<jour2:
    if mois1<mois2:
      if annee1<=annee2:
        res=-1
  else:
    if jour1>jour2:
      if mois1>mois2:
        if annee1>=annee2:
          res=1
    else:
      if jour1==jour2:
        if jour1==jour2:
          if annee1==annee2:
            res=0
  return res