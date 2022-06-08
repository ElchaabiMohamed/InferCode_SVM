def sousChaine(s1,s2):
  i=0
  j=0
  while i<len(s2) and j<len(s1): 
    if s2[i]==s1[j]:
      j+=1
    else:
      j=0
    i+=1
  return j==len(s1)