def motPalindrome(mot):
  i=0
  res=True
  while i <len(mot) and res==True:
    if mot[i] != mot[-i-1]:
      res=False
    i=i+1
  return res