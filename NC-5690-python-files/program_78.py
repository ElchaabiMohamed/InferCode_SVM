def stockerChiffres(nombre):
  res = []
  for nb in str(nombre):
    res.append(int(nb))
  res.reverse()
  return res 