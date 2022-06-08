def stockerChiffres(nombre):
  nombre = str(nombre)
  i = len(nombre)
  res = []
  while i > 0:
    res.append (int(nombre[i]))
    i = i - 1 
  return res