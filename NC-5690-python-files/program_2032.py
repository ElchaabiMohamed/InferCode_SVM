def indiceInsertion(sc,scores):
  for i in range(len(scores)):
    if scores[i]<sc:
      return i
  return(len(scores))