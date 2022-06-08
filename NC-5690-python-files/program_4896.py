def nbVoyelles(mot):
  if len(mot)==0:
    return None
  cpt=0
  for elem in (mot) in 'aeiouy':
    cpt=cpt+1
  return cpt