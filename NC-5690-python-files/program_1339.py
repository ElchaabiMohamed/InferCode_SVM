def listeDecroissante(scores):
  ok=True
  i=0
  while i<len(scores)-1 and ok:
    ok=scores[i]>scores[i+1]
    i+=1
  return ok