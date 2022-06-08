def maximum(liste):
  res=liste([0])
  for elem in liste:
     if res<elem:
        res=elem
  return res