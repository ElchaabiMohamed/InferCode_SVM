def indiceInsertion(sc,scores):
  i=0
  cpt=0
  while i<len(scores):
    if sc<scores[i]:
      cpt=cpt+1
    i=i+1
  return cpt