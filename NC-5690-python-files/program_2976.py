def indiceInsertion(sc,scores):#exo 8
  i=0
  while i<len(scores):
    if sc>=scores[i]:
      return i
    i=i+1
  return i