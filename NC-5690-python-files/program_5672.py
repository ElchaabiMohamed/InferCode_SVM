def reconstruireChainePartielle(s,n):
  res=" "
  for i in range(0,len(s),2):
    res=res+s[i]
  return res