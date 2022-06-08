def indiceInsertion(sc,scores):
  i=0
  c=True
  while i<len(scores) and c:
    if sc>=scores[i]:
      res=i+1
      c=False
    i+=1
  return res