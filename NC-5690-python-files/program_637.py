def indiceInsertion(sc,scores):
  cpt = 0
  while cpt<len(scores) & scores[cpt]>sc :
    cpt+=1
  return cpt