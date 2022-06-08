def nbVoyelles(mot):
  cpt=0
  for l in mot:
    if l in 'aeiouy':
      cpt=cpt+1
  return cpt