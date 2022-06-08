def phrasePalindrome(phrase):
  i=0
  mot=[]
  phrs=[]
  mts=True
  faute=False
  while i<len(phrase):
    if phrase[i]!=" " and mts==True:
      mot+=phrase[i]
    elif phrase[i]==" ":
      mts=False
    elif phrase[i]!=" ":
      phrs+=phrase[i]
    i+=1
  while i<len(mot) and faute==False:
    if mot[i]==phrs[-i-1]:
      res=True
    else:
      res=False
      faute==True
  return res