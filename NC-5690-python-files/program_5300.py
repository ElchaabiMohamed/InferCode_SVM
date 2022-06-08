def permutationListe(liste,permutation):
  res=[]
  for i in liste:
    liste[i]=permutation[i]
  return res