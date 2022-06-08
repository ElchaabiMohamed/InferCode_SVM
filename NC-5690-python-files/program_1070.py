def reconstruireChainePartielle(s,n):
  res=""
  for i in range(0,len(s),n):
    res=res+[i]
  return res