def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  res= 0
  if jour1 < jour2 and mois1 <= mois2 and annee1 <= annee2:
    res= res -1
  if jour1 == jour2 and mois1 == mois2 and annee1 == annee2:
    res= res + 0
  if jour1 > jour2 and mois1 >= mois2 and annee1 >= annee2:
    res= res + 1
    
  return res
  
 