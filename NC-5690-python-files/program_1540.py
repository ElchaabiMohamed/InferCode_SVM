def phrasePalindrome(phrase):
  i=0
  mot=[]
  while i<len(phrase):
    if phrase[i]==phrase[-i-1]:
        res=True
    else:
        res=False
    i+=1
  return res