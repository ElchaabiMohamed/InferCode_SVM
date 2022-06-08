def rendezVous(debut1,fin1,debut2,fin2):
  if debut1==debut2:
    res=True
  else:
    for debut1 in range(fin2):
      if fin1>fin2:
        res=False
      else:
        res=True
     
      
  return res
  