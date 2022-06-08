def motPalindrome(mot):
  res = True
  i = 0
  while i < len(mot)/2 and res == True :
    if mot[i] != mot[len(mot)-i-1] :
      res = False
    i = i + 1
  return res