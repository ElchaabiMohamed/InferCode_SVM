def listeDecroissante(scores):
  ok=True
  i=0
  if len(scores)>1:
    while i<len(scores)-1:
      if scores[i]>scores[i+1]:
        ok=False
      i=i+1
  return ok