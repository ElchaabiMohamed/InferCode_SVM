def maximum(liste):
  res=0	
  for elem in liste:
    if res<elem(liste):
      res=elem(liste)
  
    return res
  