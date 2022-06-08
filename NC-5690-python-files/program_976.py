def phrasePalindrome(phrase):
  res=True
  i=0
  j=len(phrase)-1
  while i<j and res:
    if phrase[i]==' ':
      i+=1
    elif phrase[j]==' ':
      j-=1
    elif phrase[i]!=phrase[j]:
      res=False
    else:
      i+=1
      j-=1
  return res