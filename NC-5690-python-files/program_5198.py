def phrasePalindrome(phrase):
  i=0
  end=False
  res=True
  while i<len(phrase) and end==False:
    if phrase[i]==" ":
      end=True
    elif phrase[i]==phrase[-i-1]:
      res=True
    elif phrase[-i-1]==" ":
      if phrase[i]==phrase[-i-2]:
        res=True
    else:
      res=False
    i+=1
  return res