def stockerChiffres(nombre):
  nombre = str(nombre)
  i = 0
  res = []
  while i < len(nombre):
    res = [int(nombre[i])] + res
    i = i + 1 
  return res