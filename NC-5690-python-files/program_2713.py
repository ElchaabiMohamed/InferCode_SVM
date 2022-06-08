def rendezVous(debut1,fin1,debut2,fin2):
  if debut1==debut2 or fin1==fin2:
    return True
  elif fin1>=debut2 and debut1<fin2:
    return True
  else:
    return False