def indiceInsertion(sc,scores):
  cpt = 0
  while scores[cpt]>sc & cpt<len(scores):
    cpt+=1
  return cpt