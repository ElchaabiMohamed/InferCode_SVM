def phrasePalindrome(phrase):
  ok=True
  l=[]
  i0=0
  i=0
  j=len(l)-1
  while i0<len(phrase) :
    if i0!='':
      l.append(phrase[i0])
    i0+=1
      
  while i<j and ok :
    if l[i]!=l[j] :
      ok=False
    i+=1
    j-=1
  return ok