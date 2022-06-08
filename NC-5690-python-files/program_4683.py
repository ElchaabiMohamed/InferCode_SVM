def phrasePalindrome(phrase):
  res=True
  i=0
  while i<len(phrase) and res:
    if phrase[i]!=phrase[-i-1]:
      res=False
    else:
      if len(phrase)%2=='abcdefghijklmnopqrstuvwxyz':
        res=True
  return res