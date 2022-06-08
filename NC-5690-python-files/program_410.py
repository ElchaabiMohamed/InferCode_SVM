def permutationChaine(mot):
  res=""
  for k in range(0,len(mot)-1,2):
    res=mot[k+1]+mot[k]

  return res