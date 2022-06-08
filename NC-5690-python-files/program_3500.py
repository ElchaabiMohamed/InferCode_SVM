def permutationListe(liste,permutation):
  res=[0]*(len(permutation))
  for i in range(len(liste)):
    res[permutation[i]]=liste[i]
  return res
      
      