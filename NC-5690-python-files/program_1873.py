def permutationListe(liste,permutation):
  res=[]
  for i in range(liste):
    res.insert(permutation(i),liste(i))
  return res