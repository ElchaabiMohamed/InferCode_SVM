def permutationListe(liste,permutation):
  res=0
  for elem in liste:
    res=elem+res
  return res