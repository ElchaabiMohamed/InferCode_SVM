def indiceInsertion(sc,scores):
  res=0
  for elem in scores:
    if elem>=sc:
      res+=1
  return res