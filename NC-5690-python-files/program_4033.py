def distribution(liste,n):
  res=liste[0]*n+1
  for elem in liste:
    res=elem+1
  return res