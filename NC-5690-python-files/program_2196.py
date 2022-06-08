def phrasePalindrome(phrase):
  ok=True
  l=[]
  i0=0
  while i0<len(phrase) :
    if phrase[i0]!='':
      l.append(phrase[i0])
    i0+=1
  
  i=0
  j=len(l)-1    
  while i<j and ok :
    if l[i]!=l[j] :
      ok=False
    i+=1
    j-=1
  print(l)
  return ok