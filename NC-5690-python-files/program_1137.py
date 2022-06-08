def motPalindrome(mot):
  res=0
  ok=True
  while i<len(mot) and ok:
    if mot[i]!=mot[-i-1]:
      ok=False
    i=i+1
  return ok