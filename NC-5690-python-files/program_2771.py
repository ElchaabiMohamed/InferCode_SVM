def compteChiffre(c,n):
  cpt=0
  if c==n:
    cpt+=1
  else:
    while n!=0:
      if c==n%10:
        cpt+=1
      n=n//10
  return cpt