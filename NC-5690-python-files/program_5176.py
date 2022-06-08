def listeDecroissant(scores):
  ok=True
  i=0
  while i<len(scores)-1 and ok:
    if scores[i]<scores[i+1]:
      ok=False
    i+=1
  return ok