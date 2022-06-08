def motPalindrome(mot):
  i=0
  c=True
  while i<(len(mot)/2) and c:
    if mot[i]==mot[len(mot)-i-1]:
      c=True
    else:
      c=False
    i=i+1
  if c==True:
    return True
  else:
    return False
    
    

