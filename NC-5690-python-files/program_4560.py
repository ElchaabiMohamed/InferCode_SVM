def reconstruireChainePartielle(s,n):
  if s=='':
    res=s
  for i in range(s,n):
    res=res+s[i]
  return res