def rendezVous(debut1,fin1,debut2,fin2):
  if debut2<fin1<fin2 or debut1<fin2<fin1 or debut1<debut2<fin1 or debut2<debut1<fin2:
    return True
  else:
    return False