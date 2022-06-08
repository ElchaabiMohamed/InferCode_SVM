def nbVoyelles(mot):
  if len(mot)==0:
    voy=0
  else:
    voy=0
    for elem in mot:
      if elem in ["a","e","i","o","u","y"]:
        voy=voy+1
  return voy