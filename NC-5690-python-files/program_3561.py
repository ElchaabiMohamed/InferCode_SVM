def permutationListe(liste,permutation):
  res=[0]*len(liste)
  for elem in permutation and i in range(len(liste)):
      res[elem]=liste[i]
  return res