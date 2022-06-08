def indiceInsertion(sc,scores):
  res=0
  i=0
  while i<len(joueurs):
    if sc>scores[i]:
      res=i
    i=i+1
  return res
