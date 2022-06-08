def maximum(liste):
  res=liste[0]
  for c in liste:
    if c>=res:
      res=c
  return res