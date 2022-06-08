def listeDecroissante(scores):
  i=0
  ok=True
  while i<(len(scores)-1) :
    if scores[i]<scores[i+1] :
      ok=False
    i+=1
  return ok