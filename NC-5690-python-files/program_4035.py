def permutationListe(liste,permutation):
  res=len(liste)*[0] # initialisation de res
  for i in range(len(liste)):
    res[permutation[i]]=liste[i]
  return res
    