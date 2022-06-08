def nbVoyelles(mot):
  voyel="aeiouy"
  if len(mot)==0:
    voy=None
  else:
    voy=0
    for i in range(mot[i]):
      if voyel[i] == mot[i]:
        voy=voy+1
  return voy