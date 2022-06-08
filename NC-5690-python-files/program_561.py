def phrasePalindrome(phrase):
  i=0
  mot=[]
  mts=True
  while i<len(phrase):
    if phrase[i]!=" " and mts==True:
      mot+=phrase[i]
    elif phrase[i]==" ":
      mts=False
    elif phrase[i]!=" ":
      phrs+=phrase[i]
    i+=1
  while i<len(mot) and res==True:
    if mot[i]==phrs[-i-1]:
      res=True
    else:
      res=False
  return res