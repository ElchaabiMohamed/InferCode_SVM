def sousChaine(s1,s2):
  res=True
  i=0
  j=0
  while i!=j:
    i+=1
    j+=i  
  while i<len(s1)==j<len(s2) and res:
    res=True
  else:
    res=False
  return res