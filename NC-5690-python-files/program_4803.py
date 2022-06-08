def indiceInsertion(sc,scores):
  i=0
  j=-1
  res=None
  while i<len(scores) and j<len(scores) and res==None:
    if sc>=scores[i]:
      res=i
    elif sc<scores[-1]:
      res=scores[j]
    i=i+1
  return res