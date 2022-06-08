def reconstruireChainePartielle(o,n):
  res=""
  for i in range(len(o),n):
    res=res+o[i]
  return res