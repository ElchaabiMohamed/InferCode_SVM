def reconstruireChainePartielle(s,n):
  res=''
  for i in range(0,len(s)-1,n):
    res=res+s[i]
  return res