def phrasePalindrome(phrase):
  res = True
  phrase2 = []
  for i in range (len(phrase)):
    if phrase[i] != ' ':
      phrase2.append (phrase[i])
  i = 0
  while i < len(phrase2)/2 and res == True :
    if phrase2[i] != phrase2[len(phrase2)-i-1] :
      res = False
    i = i + 1
  return res
 