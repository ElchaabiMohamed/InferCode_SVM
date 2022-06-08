def compteChiffre(chiffre,nombre):
  trouve=False
  i=0
  cpt=0
  res=None
  while i<len(l) and not trouve:
    if l[i]==x:
      cpt=cpt+1
    if cpt==n:
      trouve=True
      res=i
  i=i+1
  return res