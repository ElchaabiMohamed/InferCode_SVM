def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  if jour1 < jour2 and mois1 < mois2 and annee1 < annee2:
    res= -1
  elif jour1 == jour2 and mois1 == mois2 and annee1 == annee2:
    res= 0
  else:
    res= 1
    
    return res
  
  assert compareDates(10, 1, 2020, 14, 2, 2020)== -1 , "pb avec compareDates(10, 1, 2020, 14, 2, 2020)"
  assert compareDates(14, 2, 2020, 11, 2, 2020)== 1 , "pb avec compareDates(14, 2, 2020, 11, 2, 2020)"
  assert compareDates(10, 1, 2020, 10, 1, 2020)== 0 , "pb avec compareDates(10, 1, 2020, 10, 1, 2020)"