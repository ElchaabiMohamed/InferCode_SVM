def reconstruireChainePartielle(s,n):
  if s=='':
    res=None
  else :
    for i in range (0,len(s),n):
      res=res + s[i]
  
  return res

