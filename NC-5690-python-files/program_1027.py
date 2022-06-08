def sousChaine(s1,s2):
  res=True
  i=0
  j=0
  while i<len(s1) and j<len(s2):
    if s2[j]==' ':
      j+=1
    if s1[i]==s2[j]:
      i+=1
    j+=1
  if i!=len(s1):
    res=False
  return res