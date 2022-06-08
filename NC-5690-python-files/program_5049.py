def rendezVous(debut1,fin1,debut2,fin2):
  res=True
  if debut1>fin2 or debut2>fin1:
    res=False
  return res