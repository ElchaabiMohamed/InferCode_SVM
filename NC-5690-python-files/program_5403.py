def listeDecroissante(scores):
  res=True
  i=0
  while i<len(scores)-1:
    if scores[i]<scores[i+1]:
      return False
    i=i+1
  return res