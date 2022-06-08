def compteChiffre(c,n):
  cpt=0
  while n!=0:
    if c==n%10:
      cpt+=1
    n=n//10
  return cpt