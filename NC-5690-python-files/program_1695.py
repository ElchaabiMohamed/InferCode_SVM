def doubleChiffre(nombre):
  nombre = str(nombre)
  res = False
  i = 0
  while res == False and i < len(nombre)-1:
    if nombre[i] == nombre[i+1]:
      res = True
    i+=1

  return res