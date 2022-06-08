def distribution(liste,n):
  compte=[0]*(n+1)
  for element in liste:
    compte[element]=compte[element]+1
  return compte
    