def motPalindrome(mot):
  res=True
  i=0
  while i<int(len(mot)/2) and res:
    if mot[i]!=mot[-1-i]:
      res=False
    i+=1
  return res