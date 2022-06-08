def rendezVous(debut1,fin1,debut2,fin2):
  if debut1>=debut2 and debut1<=fin2:
    res=True
  elif fin1>=debut2 and fin1<=fin2:
    res=True
  else:
    res=False
  return res