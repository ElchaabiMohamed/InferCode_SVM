def listeSymetrique(l):
  res = True
  i = 0
  while i < len(l)/2 and res == True :
    if l[i] != l[len(l)-i-1] :
      res = False
    i = i + 1
  return res

def stockerChiffres(nombre):
  if nombre == 0 :
    res = [0]
  else :
    res = []
  while nombre != 0 :
    res.append (nombre%10)
    nombre = nombre//10
  return res

def nombreSymetrique (nombre):
  liste = stockerChiffres(nombre)
  res = listeSymetrique(liste)
  return res