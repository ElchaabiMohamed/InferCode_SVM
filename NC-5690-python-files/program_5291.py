def indiceInsertion(sc,scores):
  i=0
  trouve=False
  res=0
  while i<len(scores) and not trouve :
    if sc>scores[i] :
      trouve=True
    i+=1
  res=i
  return res