def motPalindrome(mot):
  palindrome = True
  i=0
  j=len(mot)-1
  i=0
  while i<j and palindrome :
    if mot[i] != mot[j]:
      palindrome = False
    i=i+1
    j=j-1
  return palindrome