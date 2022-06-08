def indiceInsertion(sc,scores):
  i=0
  c=True
  res=0
  while i<len(scores) and c:
    if sc>=scores[i]:
      res=i+1
      c=False
    i+=1
  return res