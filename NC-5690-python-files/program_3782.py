def sousChaine(s1,s2):
  j=0
  i=0
  if s1=='':
    res=True
  while j<len(s2) and i<len(s1):
    if s1[i]==s2[j]:
      i=i+1
    j=j+1
  if len(s1)==i:
    return True
  else:
    return False
      