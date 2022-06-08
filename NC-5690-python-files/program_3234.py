def listeDecroissante(scores):
  res=True
  if scores==[]:
    res=True
  for i in range(len(scores)-1):
    if scores[i]<=scores[i+1]:
      res=False
  return res