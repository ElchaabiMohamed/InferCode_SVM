def phrasePalindrome(phrase):
  ok=True
  i=0
  fin=False
  while i<len(phrase) and fin==False:
    if phrase[i]=='':
      fin==True
    elif phrase[i]==phrase[-i-1]:
      ok=True
    elif phrase[i]=='':
      if phrase[i]==phrase[-i-2]:
        ok=True
    else:
      ok=False
    i=i+1
  return ok