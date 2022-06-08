def permutationListe(liste,permutation):
  res=[0]*(len(liste)+1)
  for i in liste:
    permutation[i]=liste[i] 
  return res