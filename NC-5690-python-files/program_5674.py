def rendezVous(debut1,fin1,debut2,fin2):
  if fin1>=debut2:
    if fin2>=debut1:
      res=True
    else:
      res=False
  else:
    res=False
  return res