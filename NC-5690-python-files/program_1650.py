def maximum(liste):
  res=liste[0]
  for i in liste:
    if res<liste[i]:
      res=liste[i]
    return res