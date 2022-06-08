def sousChaine2(s1,s2):
  i=0
  j=0
  cpt=0
  while i<len(s2) and j<len(s1): 
    if s2[i]==s1[j]:
      cpt+=1 
      j+=1
    else:
      cpt=0
      j=0
    i+=1
  return cpt==len(s1)