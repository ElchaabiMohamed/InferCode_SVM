def nbVoyelles(mot):
  cpt=0
  for i in mot:
    if i in 'aeiouy':
      cpt+1
  return cpt