def compteChiffre(chiffre,nombre):
  cpt=0
  i=0
  l=[]
  while nombre!=0:
    nombre=nombre//10
    l.append(nombre)
  while i<len(l):
    if l[i]==chiffre:
      cpt=cpt+1
  return cpt