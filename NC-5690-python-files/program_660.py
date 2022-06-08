def indiceInsertion(sc,scores):
  res=0
  for elem in scores:
    if sc>=elem:
      res+=1
    return res