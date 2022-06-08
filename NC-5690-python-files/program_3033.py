def nbVoyelles(mot):
  if len(mot)==0:
    voy=None
  else:
    voy=0
    for i in mot:
      if mot in ["a","e","i","o","u","y"]:
        voy=voy+1
  return voy