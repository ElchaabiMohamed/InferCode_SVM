def phrasePalindrome(phrase):
  i=0
  c=True
  while i<(len(phrase)/2) and c:
    if phrase[i]!=' ' or phrase[i]!=',' or phrase[i]!="'":

      if phrase[i]==phrase[len(phrase)-i-1]:
        c=True
      else:
        c=False
    i=i+1
  if c==True:
    return True
  else:
    return False