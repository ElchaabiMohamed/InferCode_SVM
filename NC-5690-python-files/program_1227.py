def listeDecroissante(scores):
  ok=True
  i=0
  while i<len(scores)-1:
    if scores[i]>score[i+1]:
      ok=False
    i=i+1
  return ok