def permutationListe(liste,permutation):
  if len(liste)==len(permutation):
    for i in range(len(liste)):
      liste[permutation[i]]=liste[i]
  return liste