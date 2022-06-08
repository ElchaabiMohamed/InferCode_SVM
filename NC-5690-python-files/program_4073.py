def phrasePalindrome(phrase):
  i=0
  ok=True
  while i<len(phrase)/2 and ok:
    if phrase[i]==' ':
      i+=1
    if phrase[-i-1]==' ':
      i+=1
    elif phrase[i]!=phrase[-i-1]:
      ok=False
    i+=1
  return ok