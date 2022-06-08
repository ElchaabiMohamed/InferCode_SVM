def indiceInsertion(sc,scores):
  res=0
  i=0
  while i<len(scores) and sc<scores[i]:
    i=i+1 
  return i-1