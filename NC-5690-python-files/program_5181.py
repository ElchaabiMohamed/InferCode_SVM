def nbVoyelles(mot):
  voyel="aeiouy"
  if len(mot)==0:
    voy=None
  else:
    voy=0
    for i in range(len(mot)):
      if mot[i]==voyel[i]:
        voy=voy+1
  return voy