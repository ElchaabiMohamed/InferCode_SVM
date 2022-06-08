def motPalindrome(mot):
  ok=True
  i=0
  j=len(mot)-1
  while i<j and ok:
    if mot[i]!=mot[j]:
      ok=False
    i+=1
    j-=1
  return ok
    