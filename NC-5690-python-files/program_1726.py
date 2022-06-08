def phrasePalindrome(phrase):
  ok=False
  i=0
  while i<len(phrase)//2:
    if phrase[i]==" " and phrase[-i]==" ":
      i+=1
    elif phrase[i]!=phrase[-i-1]:
      ok=False
      i+=1
    else:
      ok=True
      i+=1
  if phrase=="":
    ok=True
  return ok