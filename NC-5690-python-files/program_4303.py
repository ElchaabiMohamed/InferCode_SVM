def stockerChiffres(nombre):
  nombre = str(nombre)
  i = 0
  res = []
  while i < len(nombre):
    res.append (int(nombre[i]))
    i = i + 1 
  return res