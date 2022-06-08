def indiceInsertion(sc,scores):
  i=0
  while i<len(scores):
    if sc>scores[i]:
      return i
    i=i+1
  if sc<score[i]:
      return len(scores)