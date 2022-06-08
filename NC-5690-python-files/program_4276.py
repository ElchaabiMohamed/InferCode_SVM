def phrasePalindrome(phrase):
  ok=True
  i=0
  j=0
  while i<len(phrase)//2 and j<len(phrase)//2 and ok:
    if phrase[i]==" ":
      i+=1
    elif phrase[-j-1]==" ":
      j+=1
    elif phrase[i]==phrase[-j-1]:
      ok=True
      i+=1
      j+=1
    else:
      ok=False
  if phrase=="":
    ok=True
  return ok