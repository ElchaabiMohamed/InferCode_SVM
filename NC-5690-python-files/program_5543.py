def rendezVous(debut1,fin1,debut2,fin2):
  if debut1 <= debut2 and fin1 >= debut2 :
    res = True
  elif debut2 <= debut1 and fin2 >= debut1 :
    res = True
  else :
    res = False
  return res