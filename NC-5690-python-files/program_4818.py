def distribution(liste,n):
  cpt=[0]*4
  for elem in liste:
    cpt=cpt[elem]+1
  return cpt 