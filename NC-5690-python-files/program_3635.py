def reconstruireChainePartielle(s,n):
  res=''
  for i in range(0,s,n):
    res=res+s[i]
  return res