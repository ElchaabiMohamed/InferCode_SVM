def permutationListe(liste,permutation):
  res=liste[0]
  for elem in liste:
    res[elem]=liste[0]
  return res