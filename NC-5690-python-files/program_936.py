def minimum(liste):
  res=len([0])
  for elem in liste:
    if res>elem:
      res=elem
  return res