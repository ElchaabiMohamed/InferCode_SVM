def indiceInsertion(sc,scores):
  res=0
  i=0
  while i<len(scores) and sc<scores:
    res=i
    i=i+1
  return res