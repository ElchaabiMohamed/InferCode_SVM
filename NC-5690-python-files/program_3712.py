def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  date1 = int(str(annee1) + str(mois1) + str(jour1))
  date2 = int(str(annee2) + str(mois2) + str(jour2))
  
  if date1 > date2 :
    res = 1 
  elif date1 < date2 :
    res = -1
  else :
    res = 0
  return res