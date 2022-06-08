def rendezVous(debut1,fin1,debut2,fin2):
  res=0
  if debut1>fin2 and debut2>fin1:
    res=FALSE 
  else:
    res=TRUE
  return res