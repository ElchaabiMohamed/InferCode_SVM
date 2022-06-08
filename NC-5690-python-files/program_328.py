def listeDecroissante(scores):
  res=True
  if len(scores)==0:
    return res
  else:
    x=scores[0]
    for elem in scores:
      if x<elem:
        res=False
      x=elem
    return res