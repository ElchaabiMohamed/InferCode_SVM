def phrasePalindrome(phrase):
  ok=False
  i=0
  while i<len(phrase) and not ok:
    if phrase[i]!=phrase[-i-1]:
      ok=True
    i+=1
  if phrase=="":
    ok=True
  return ok