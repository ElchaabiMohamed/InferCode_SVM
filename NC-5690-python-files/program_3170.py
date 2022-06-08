def distribution(liste,n):
  res=[]
  cpt=[0]*(n+1)
  for elem in liste:
    cpt[elem]=cpt[elem]+1
  return res
