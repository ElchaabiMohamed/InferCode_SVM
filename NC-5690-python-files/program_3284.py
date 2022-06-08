def motPalindrome(mot):
  palindrome=True
  i=0
  while i<len(mot) and palindrome==True:
    if mot[i]!=mot[-i-1]:
      palindrome=False
    i=i+1
  return palindrome