def indiceInsertion(sc,scores):
  cpt = 0
  while cpt<len(scores) & scores[cpt]>sc :
    print(cpt)
    cpt+=1
  return cpt