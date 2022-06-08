def indiceInsertion(sc,scores):
  i=0
  trouve=False
  cpt=0
  while i<len(scores) and not trouve :
    if sc>scores[i] :
      trouve=True
    else :
      cpt+=1
    i+=1
  return cpt