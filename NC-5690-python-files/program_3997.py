def nombreSymetrique(nombre):
  i=0
  temp=str(nombre)
  while i<len(temp):
    if temp[i]!=temp[-(1+i)]:
      return False
    i+=1
  return True