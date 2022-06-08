def nbVoyelles(mot):
  cpt=0
  for i in mot: 
    if i=='aeiouy':
      cpt=cpt+1
  return cpt