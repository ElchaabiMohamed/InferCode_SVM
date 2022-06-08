def rendezVous(debut1,fin1,debut2,fin2):
  if fin1>=debut2 and debut1<fin2:
    return True
  else:
    return False
  
rendezVous(1,10,7,20)
rendezVous(1,7,10,20)