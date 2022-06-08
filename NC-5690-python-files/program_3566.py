def phrasePalindrome(phrase):
  ok=True
  i=0
  j=0
  ch=''
  while j<len(phrase) :
    if 'a'<= phrase[j] and phrase[j]<='z' and phrase[j]!='' :
      ch+=phrase[j]
    j+=1

  while i<len(ch):
    if ch[i]!=ch[-i-1]:
      ok=False
    i+=1
  return ok