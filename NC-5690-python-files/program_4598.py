def phrasePalindrome(phrase):
  ok=True
  i=0
  while i<len(l)//2 and ok:
    if l[i]!=l[-i-1]:
      ok=False
    i+=1
  return ok