def listeDecroissante(scores):
  ok=True
  while i<len(scores) and ok:
    if scores[i]>=scores[i+1]:
      res=ok
    else:
      res=False
  return res