def permutationListe(liste,permutation):
  res=[]
  for i in liste:
    res[permutation]=liste[i]
  return res