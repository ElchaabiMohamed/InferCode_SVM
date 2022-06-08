def nbChiffres(n):
  cpt=0
  if n==0:
    cpt=1
  else:
    while n!=0:
      n=n//10
      cpt+=1
  return cpt