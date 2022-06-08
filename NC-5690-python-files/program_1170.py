def listeDecroissante(scores):
  res=False
  if scores==[]:
    res=True
  for i in range(len(scores)):
    if scores[i]>scores[1+i]:
      res=True
  return res