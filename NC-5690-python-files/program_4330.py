def listeDecroissante(scores):
  c=True
  i=0
  while i<(len(scores)-1) and c:
    if scores[i]<scores[i+1]:
      c=False
    i=i+1
  return c