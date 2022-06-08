def listeDecroissante(scores):
  scorePrec=scores[0]
  ok=True
  i=1
  while i<len(scores) and ok:
    if scorePrec<=scores[i]:
      ok=False
    i+=1
  return ok