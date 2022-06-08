def phrasePalindrome(phrase):
  ok=True
  i=0
  j=0
  l=[]
  while j<len(phrase) :
    if 'a'<= phrase[j] and phrase[j]<='z' and phrase[j]!='' :
      l.append(phrase[j])
    j+=1

  while i<len(l):
    if phrase[i]!=phrase[-i-1]:
      ok=False
    i+=1
  return ok