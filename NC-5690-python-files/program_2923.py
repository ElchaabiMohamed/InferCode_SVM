def phrasePalindrome(phrase):
  res=True
  i=0
  j=len(phrase)-1
  while i<len(phrase):
    if phrase[i]==' ':
      i+=1
    if phrase[j]==' ':
      j-=1
    if phrase[i]!=phrase[j]:
      res=False
    i+=1
    j-=1
  return res