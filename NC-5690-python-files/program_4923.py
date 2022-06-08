def phrasePalindrome(phrase):
  res=True
  i=0
  while i<len(phrase) and res:
    if phrase[i]!=phrase[-i-1]:
      res=False
    i+=1
  return res