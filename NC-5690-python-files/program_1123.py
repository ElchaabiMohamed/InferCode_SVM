def rendezVous(debut1,fin1,debut2,fin2):
  res=0
  if debut1>=debut2 or fin1<=fin2:
    if fin1>=debut2:
      res=True
  else:
    res=False
  return res