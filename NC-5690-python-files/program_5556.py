def distribution(liste,n):
  res=[0]*(n+1)
  for elem in liste:
    res[elem]=res+1
  return res