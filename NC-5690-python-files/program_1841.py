def stockerChiffres(nombre):
  res=[]
  cpt=0
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
    cpt+=1
  if cpt==0:
    res.append(0)
  return res
def listeSymetrique(l):
  trouve=True
  i=0
  j=len(l)-1
  while i<len(l) and j<len(l) and trouve:
    if l[i]!=l[j]:
      trouve=False
    i+=1
    j-=1
  return trouve
def nombreSymetrique(nombre):
  res=stockerChiffres(nombre)
  trouve=listeSymetrique(res)
  return trouve