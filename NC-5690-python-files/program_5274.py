def listeDecroissante(scores):
  res=False
  if scores==[]:
    res=True
  for i in range(len(scores)-1):
    if scores[i]>scores[1+i]:
      res=True
  return res