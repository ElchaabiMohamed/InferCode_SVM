def reconstruireChainePartielle(s,n):
  if s=='':
    res=s
  for i in range(s,n):
    res=res+i
  return res