def indiceInsertion(sc,scores):
  i=0
  res=0
  while i<len(scores):
    if sc>=scores[i]:
      res=i
    i=i+1
  return res