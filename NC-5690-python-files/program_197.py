def indiceInsertion(sc,scores):
  cpt = 0
  while scores[cpt]>sc:
    cpt+=1
  return cpt