def indiceInsertion(sc,scores):
  i=0
  res=0
  while i<len(scores):
    if scores[i]<sc:
      return i
    i+=1
  if res==0:
    res=len(scores)
  return res