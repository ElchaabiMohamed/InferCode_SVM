def listeDecroissante(scores):
  if scores==[]:
    ok=True
  else:
    scorePrec=scores[0]
    ok=True
    i=1
    while i<len(scores) and ok:
      if scorePrec<=scores[i]:
        ok=False
      scorePrec=scores[i]
      i+=1
  return ok