def permutationListe(liste,permutation):
  res=[]*(len(permutation))
  for i in range(len(liste)):
    permutation[i]=liste[i] 
  return res