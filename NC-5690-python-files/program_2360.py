def motPalindrome(mot):
  ok=True
  i=0
  j=len(mot)-1
  while i<len(mot) and ok:
    if i==j:
      ok=True
    else:
      ok=False
    i=i+1
    j=j-1
  return ok