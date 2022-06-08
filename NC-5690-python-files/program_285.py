def distribution(liste,n):
  cpt=[0]*(n+1)
  for elem in liste:
    cpt=cpt+liste[elem]
  return cpt