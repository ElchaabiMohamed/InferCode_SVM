def listeDecroissante(scores):
  ok=True
  i=0
  while i<len(lscore)-1 and ok:
    if lscore[i]<=lscore[i+1]:
      ok=False
    i=i+1
  return ok