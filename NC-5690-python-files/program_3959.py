def reconstruireChainePartielle(o,n):
  res=""
  for i in range(o,len(o),n):
    res=res+o[i]
  return res