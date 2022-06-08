def rendezVous(debut1,fin1,debut2,fin2):
  if debut1<fin1 and debut2<fin2:
    if debut1>fin2 or debut2>fin1:
      res=False
    else:
      res=True
  else:
    res=None
  return res