def listeDecroissante(scores):
  res=False
  if scores==[]:
    res=True
  for i in scores:
    if scores[i]>scores[i+1]:
      res=True
  return res