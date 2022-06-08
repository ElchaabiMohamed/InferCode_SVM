def compteChiffre(chiffre,nombre):
  res=0
  if nombre==0:
    res=0
  else:
    while nombre!=0:
      chiffre2=nombre%10
      if chiffre2==chiffre:
        res=res+1
      nombre=nombre//10
  return res