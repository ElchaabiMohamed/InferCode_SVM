def indiceInsertion(sc,scores):
  i=0
  while i<len(scores):
    if scores[i]<sc:
      return i
    i+=1