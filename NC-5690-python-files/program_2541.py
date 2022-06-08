def permutationListe(liste,permutation):
  res=[0]*(len(permutation))
  for i in range(len(liste)):
    res[permutation]=liste[i]
  return res
      
      