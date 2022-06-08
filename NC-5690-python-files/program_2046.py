def nbVoyelles(mot):
  cpt=0
  for n in mot: 
    if n=='aeiouy':
      cpt=cpt+1
  return cpt