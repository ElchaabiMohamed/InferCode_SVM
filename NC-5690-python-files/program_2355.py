def permutationListe(liste,permutation):
  res=[0]
  for i in liste:
    permutation[i]=liste[i] 
  return res