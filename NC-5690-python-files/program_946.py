def nbVoyelles(mot):
  cpt=0
  for i in range(len(mot)):
    if mot[i] in 'aeiouy':
     cpt=+3
  return cpt