def phrasePalindrome(phrase):
  ok=False
  i=0
  while i<len(phrase)//2:
    if phrase[i]==" " and phrase[-i]==" ":
      ok=False
    elif phrase[i]!=phrase[-i-1]:
      ok=True
    else:
      ok=False
    i+=1
  if phrase=="":
    ok=True
  return ok