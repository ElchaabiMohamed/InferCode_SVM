def compteChiffre(chiffre,nombre):
  if chiffre==0 and nombre==0:
    res=1
  else:
    res=0
    x=nombre
    while x!=0:
      if x%10==chiffre:
        res+=1
      x=x//10
  return res