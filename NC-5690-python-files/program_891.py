def indiceInsertion(sc,scores):
  for i in range(len(scores)):
    if sc>scores[i]:
      return i+1