def reconstruireChainePartielle(s,n):
  if s=='':
    res=s
  for i in range(0,s,n):
    res=res+i
  return res