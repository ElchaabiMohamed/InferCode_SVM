def indiceInsertion(sc,scores):
  i=0
  while i<len(scores)+1:
    if sc>scores[i]:
      return i
    i=i+1