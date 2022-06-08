def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  if annee1-annee2<0:
    return -1 
  else:
    if mois1-mois2<0:
      return -1
    else:
      if jour1-jour2<0:
        return -1
      elif jour1-jour2==0:
        return 0
      else:
        return 1
      
compareDates(10,1,2020,14,2,2020)
compareDates(14,2,2020,11,2,2020)
compareDates(10,1,2020,10,1,2020)