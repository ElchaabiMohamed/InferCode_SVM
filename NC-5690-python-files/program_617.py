def motPalindrome(mot):
  res=True
  i=0
  j=len(mot)-1
  while i<len(mot) and res:
    if mot[i]!=mot[j]:
      res=False
    i=i+1
    j=j-1
  return res
