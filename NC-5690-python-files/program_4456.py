def motPalindrome(mot):
  res=False
  i=0
  while i<len(mot) and not res:
    if mot[i]==mot[-1-i]:
      res=True
    i+=1
  return res