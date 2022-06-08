def listeDecroissante(scores):
  i=0
  res=True
  while i < len(scores)-1:
    if scores[i] < scores[i+1]:
      res=False
  i=i+1
  return res