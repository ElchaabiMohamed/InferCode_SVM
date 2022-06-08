def motPalindrome(mot):
  c=True
  while i<(len(mot)/2) and c:
    if mot[i]==mot[len(mot)-i]:
      c=True
    else:
      c=False
  if c==True:
    return True
  else:
    return False
    
    

