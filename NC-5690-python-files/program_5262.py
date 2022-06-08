def distribution(liste,n):
  res=[0]*(n+1)
  for i in liste:
    res[i]+=1
  return res