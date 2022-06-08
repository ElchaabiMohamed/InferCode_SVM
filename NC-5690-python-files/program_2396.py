def nbVoyelles(mot):
  cpt=o
  for lettre in mot:
    if lettre in 'aeiouy':
      cpt=cpt+1
  return cpt
