def distribution(liste,n):
  cpt=[0]*4
  for elem in liste:
    cpt[elem]=cpt[elem]+1
  return cpt 