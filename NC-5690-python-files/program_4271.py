def reconstruireChainePartielle(s,n):
  res=""
  for i in range (0,len(mot),n):
    res=res+mot[i]
  return res