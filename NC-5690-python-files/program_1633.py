def reconstruireChainePartielle(s,o,n):
  res=""
  for i in range(s,len(o),n):
    res=res+s[i]
  return res