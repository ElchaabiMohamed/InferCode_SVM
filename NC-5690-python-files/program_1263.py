def permutationListe(liste,permutation):
  for i in range(len(liste)):
    liste[permutation[i]]=liste[i]
  return liste