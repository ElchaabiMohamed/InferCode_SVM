def nombreSymetrique(nombre):
  for nb in str(nombre):
    res.append(int(nb))
  
  return listeSymetrique(res)