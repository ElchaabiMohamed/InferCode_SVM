def indiceInsertion(sc,scores):
  i=0
  trouve=False
  while i<len(scores) and not trouve:
    trouve=scores[i]<sc
    i+=1
  return i-1