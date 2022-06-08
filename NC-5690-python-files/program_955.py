def permutationListe(liste,permutation):
  res = liste
  for i in range(len(liste)) :
    res[permutation[i]] = liste[i]
    print (res)
  return res