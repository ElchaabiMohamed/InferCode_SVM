def nbVoyelles(mot):
  voyel="aeiouy"
  if len(mot)==0:
    voy=None
  else:
    voy=0
    for i in mot:
      if voyel[i] ==mot:
        voy=voy+1
  return voy