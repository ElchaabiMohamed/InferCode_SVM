def permutationListe(liste,permutation):
  res=[0]*len(liste)
  for elem,smt in zip(liste,permutation):
    res[smt]=liste[elem]
  return res