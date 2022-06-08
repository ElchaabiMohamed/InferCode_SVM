def motPalindrome(mot):
  res=True
  i=0
  j=len(mot)-1
  while i<len(mot):
    if mot[i]!=mot[j]:
      res=False
    i+=1
    j-=1
  return res