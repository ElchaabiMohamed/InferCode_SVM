def stockerChiffres(nombre):
  temp = str(nombre)
  res = [0]*len(temp)
  for i in range(len(temp)):
    res[-(1+i)]=temp[i]
  return res