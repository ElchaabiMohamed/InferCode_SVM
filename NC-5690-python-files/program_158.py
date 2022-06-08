def phrasePalindrome(phrase):
  ok=True
  i=0
  while i<len(phrase)//2 and ok:
    if phrase[i]!=phrase[-i-1]:
      ok=False
    i+=1
  return ok