def permutationListe(liste,permutation):
  res=[]
  for i in permutation:
    res.insert(permutation(i),liste(i))
  return res