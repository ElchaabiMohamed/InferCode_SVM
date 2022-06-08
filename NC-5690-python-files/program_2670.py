def phrasePalindrome(phrase):
  ok=True
  i=0
  while i<len(phrase)//2:
    if phrase[i]==" " and phrase[-i]==" ":
      i+=1
    elif phrase[i]==phrase[-i-1]:
      ok=True
      i+=1
    else:
      ok=False
      i+=1
  if phrase=="":
    ok=True
  return ok