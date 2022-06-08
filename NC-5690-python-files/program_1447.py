def stockerChiffres(nombre):
  cpt=0
  res=[]
  nb=nombre
  while nb!=0:
    res=res+[nb%10]
    nb=nb//10
  if res==[]:
    res=[0]
  return res
    
def listeSymetrique(l):
    trouve=True
    i=0
    j=-1
    while i<len(l) and j>=-len(l) and trouve!=False:
      if l[i]!=l[j]:
        trouve=False
      i=i+1
      j=j-1
    return trouve
  
def nombreSymetrique(nombre):
  l=stockerChiffres(nombre)
  res=listeSymetrique(l)
  return res
  
  