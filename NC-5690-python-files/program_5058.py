def palindrome(phrase):
  P=[]
  i=0
  c=True
  for lettre in phrase:
    if 'a'>=lettre>='z':
      P.append(lettre)
    
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