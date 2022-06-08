def phrasePalindrome(phrase):
  ok=True
  i=0
  j=0
  while i<j and ok:
    if phrase[i]=='':
      i=i+1
    if phrase[j]=='':
      j=j-1
    i=i+1
    j=j-1
    if phrase[i]!=phrase[-j-1]:
      ok=False
  return ok

  