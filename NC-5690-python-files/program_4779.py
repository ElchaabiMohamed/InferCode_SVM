def rendezVous(debut1,fin1,debut2,fin2):
  if debut1>fin2:
    res=False
  if debut2>fin1:
    res=False
  else:
    res=True
  return res