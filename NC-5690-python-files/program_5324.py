def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  if annee1==annee2 and mois1==mois2 and jour1==jour2:
    return 0
  elif annee1<=annee2 or mois1<=mois2 and jour1<jour2:
    return -1
  else:
    return 1