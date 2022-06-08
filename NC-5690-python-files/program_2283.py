def indiceInsertion(sc,scores):
  i=0
  res=None
  while i<len(scores) and res==None:
    if sc>=scores[i]:
      res=i
    elif sc<scores[-1]:
      res=scores[scores[-1]]
    i=i+1
  return res