def phrasePalindrome(phrase):
  i=0
  j=-1
  ok=True
  while i<len(phrase)/2 and j<len(phrase)/2 and ok:
    if phrase[i]==' ':
      i+=1
    if phrase[j]==' ':
      j-=1
    elif phrase[i]!=phrase[j]:
      ok=False
    i+=1
    j-=1
  return ok