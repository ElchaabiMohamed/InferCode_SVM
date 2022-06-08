def phrasePalindrome(m):
  res=True
  i=0
  j=0
  while i<len(m) and j<len(m) and res:
    if m[i]==' ':
      i+=1
    elif m[-1-j]==' ':
      j+=1
    if i==j:
      if m[i]!=m[-1-j]:
        res=False
    i+=1
    j+=1
  return res