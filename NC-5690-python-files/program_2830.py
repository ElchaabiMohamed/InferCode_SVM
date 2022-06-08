def listeDecroissante(scores):
  res=[]
  for i in range(len(scores)-1):
    if scores[i]>scores[i+1]:
      res=True
    else:
      res=False
  return res