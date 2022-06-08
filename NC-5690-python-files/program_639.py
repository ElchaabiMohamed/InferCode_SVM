def reconstruireChainePartielle(s,n):
  res=''
  for i in (len(s),n):
    res=res+s[i]
  return res