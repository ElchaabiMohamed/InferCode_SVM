def rendezVous(debut1,fin1,debut2,fin2):
  if debut2<fin1<fin2 or debut1<fin2<fin1:
    return True
  else:
    return False
assert rendezVous(6,20,12,15) 
