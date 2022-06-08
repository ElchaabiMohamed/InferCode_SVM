def phrasePalindrome(phrase):
  P=[]
  i=0
  c=True
  if a>=phrase[i]>=z:
    P.append(phrase[i])
  
  while i<(len(P)/2) and c:
    
    if P[i]==P[len(P)-i-1]:
        c=True
    else:
        c=False
    i=i+1
  if c==True:
    return True
  else:
    return False