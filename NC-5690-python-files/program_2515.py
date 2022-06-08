def phrasePalindrome(phrase):
  ok=True
  i=0
  j=-1
  while i<len(phrase) and j<-len(phrase) and ok:

    if phrase[i]==' ':
      phrase[i+1]
    if phrase[j]==' ':
      phrase[j-1]

    if phrase[i]!=phrase[j]:
      ok=False
    i+=1
    j-=1
  return ok
