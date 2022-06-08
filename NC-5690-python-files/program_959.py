def maximum(liste):
  res= -12
  for elem in liste:
    if  res < elem:
      res=elem
  return res