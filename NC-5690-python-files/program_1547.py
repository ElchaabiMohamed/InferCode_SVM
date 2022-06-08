def distribution(liste,n):
  res=[n+1]
  for i in range (liste):
    if i==res[i]:
      res[i]=res[i]+1
  
  return res

