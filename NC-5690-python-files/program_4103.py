def motPalindrome(mot):
  i=0
  trouve=False
  res=True
  while i<len(mot)/2 and not trouve:
    if mot[i]==mot[-i-1]:
      i+=1
      trouve=True
  if trouve: 
    res=True
  return res