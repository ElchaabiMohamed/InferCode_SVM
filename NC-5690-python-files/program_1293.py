def motPalindrome(mot):
  ok=True
  i=0
  while i<len(mot) and ok:
    ok=mot[i]==mot[-1-i]
    i+=1
  return ok   