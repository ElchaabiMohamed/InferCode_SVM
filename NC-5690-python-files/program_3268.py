def phrasePalindrome(phrase):
  ok=True
  i=0
  j=0
  while i<len(phrase) and ok:
    if phrase[i]==' ':
      i+=1
    elif phrase[j]==' ':
      j-=1
    ok=phrase[i]==phrase[j]
    i+=1
    j-=1
  return ok