def listeDecroissante(scores):
  res=True
  x=scores[0]
  for elem in scores:
    if x<elem:
      res=False
    x=elem
  return res