def permutationListe(liste,permutation):
  res=[0]*len(liste)
  for elem,valeur in zip(permutation,liste):
      res[elem]=valeur
  return res