def permutationListe(liste,permutation):
  res=[]
  for i in range(permutation):
    res.insert(permutation(i),liste(i))
  return res