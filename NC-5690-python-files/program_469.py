def distribution(liste,n):
  res=[0]*(n+1)
  for elem in liste:
    if 0<=elem<=n:
      res[elem]+=1
  return res