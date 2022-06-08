def permutationListe(liste,permutation):
  res=[0]*(len(liste))
  for i in range(len(permutation)):
    res[permutation[i]]=liste[i]
  return res