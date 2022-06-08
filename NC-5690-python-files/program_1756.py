def maximum(liste):
  res=-100	
  for elem in liste:
    if res<elem:
      res=elem
  return res
  