def sousChaine(s1,s2):
  res=True
  i=0
  j=0
  while i!=j:
    i+=1
    j+=i  
  while i<len(s1) and j<len(s2) and res:
    if s1[i]==s2[j]:
      res=True
    i+=1
  else:
    res=False
  return res