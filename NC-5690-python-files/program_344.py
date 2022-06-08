def permutationListe(liste,permutation):
  res=[]
  for i in liste:
    res[i]=liste[permutation[i]]
  return res