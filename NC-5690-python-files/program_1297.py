def maximum(liste):
  res=-12
  for elem in liste:
    if res<elem:
      res=elem
    if elem in liste==0:
      res=None
  return res