def sousChaine(s1,s2):
  res=False
  i=0
  j=0
  while i<len(s1) and j<len(s2) and s1[i]!=s2[j]:
    j+=1
  else:
    while i<len(s1) and j<len(s2) and s1[i]==s2[j]:
      if s1[i]==s2[j]:
        res=False
      i+=1
      j+=1  
  return res