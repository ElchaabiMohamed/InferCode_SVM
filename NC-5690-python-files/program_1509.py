def nbVoyelles(mot):
  if len(mot)==0:
    voy=None
  else:
    voy=0
    for i in range(len(mot)):
      if mot in "aeiouy":
        voy=voy+1
  return voy