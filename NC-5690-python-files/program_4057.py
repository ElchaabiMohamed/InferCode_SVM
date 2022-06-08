def phrasePalindrome(phrase):
  ok=False
  i=0
  j=0
  while i<len(phrase)//2 and j<len(phrase)//2:
    if phrase[i]==" ":
      i+=1
    elif phrase[-j]==" ":
      j+=1
    elif phrase[i]!=phrase[-j-1]:
      ok=False
    else:
      ok=True
    i+=1
    j+=1
  if phrase=="":
    ok=True
  return ok