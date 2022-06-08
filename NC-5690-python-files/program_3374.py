def listeDecroissante(scores):
  ok=False
  while i<len(scores) and not ok:
    if liste[i]>liste[i+1]:
      res=True
    else:
      res=ok
  return ok