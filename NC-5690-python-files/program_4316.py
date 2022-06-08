def rendezVous(debut1,fin1,debut2,fin2):
  res=True
  if fin1<debut2 or debut1>fin2:
    res=False
  return res