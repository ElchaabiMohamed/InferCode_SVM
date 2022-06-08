def distribution(liste,n):
  cpts=[0]*(n+1)
  for elem in liste:
    liste[elem]=liste[elem]+1
  return liste[elem]