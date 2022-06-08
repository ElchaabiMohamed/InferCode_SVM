def permutationListe(liste,permutation):
  res=liste[0]
  for elem in liste:
    res[permutation]=liste[elem]
  return res