def nbVoyelles(mot):
  cpt=0
  for letrre in mot:
    if lettre in 'aeiouy':
      cpt=cpt+1
  return cpt