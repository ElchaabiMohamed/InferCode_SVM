def Permutation(mot):
  res=""
  for k in range(0,len(mot),2):
    res=mot[k+1]+mot[k]

  return res