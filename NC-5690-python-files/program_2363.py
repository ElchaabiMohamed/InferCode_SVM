def rendezVous(debut1,fin1,debut2,fin2):
  if debut1>=debut2 and debut1<=fin2 :
    res=True
  elif debut2>=debut1 and debut2<=fin1 :
    res=True
  else :
    res=False
  return res