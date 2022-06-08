def nbVoyelles(mot,voyel):
  if len(mot)==0:
    voy=None
  if len(voyel)==0:
    voyel=None
  else:
    voy=0
    for i in range(len(liste)):
      if voyel[i]==liste[i]:
        voy=voy+1
  return None