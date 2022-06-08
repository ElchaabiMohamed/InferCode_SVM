def maximum(liste):
  res=0
  for i in liste:
    res=res+i
    if res<i:
      res=i
    
  return res