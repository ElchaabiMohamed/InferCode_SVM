def maximum(liste):
  res=liste[0]
  for i in liste:
    if i>=res:
      res=i
  return res