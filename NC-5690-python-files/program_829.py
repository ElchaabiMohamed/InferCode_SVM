def motPalindrome(mot):
  res=True
  i=0
  while i<len(mot):
    if mot[i]!=mot[-i-1]:
      res=False
    i=i+1
  return res