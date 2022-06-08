def maximum(liste):
  res=liste
  for elem in liste:
    if res<elem:
      res=elem
  return res