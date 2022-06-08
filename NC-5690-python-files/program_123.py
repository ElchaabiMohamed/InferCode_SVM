def indiceInsertion(sc,scores):
  i=0
  c=True
  res=0
  while i<len(scores) and c:
    if sc>=scores[i]:
      res=i
      c=False
    i+=1
    if c:
      res=len(scores)
  return res