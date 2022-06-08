def nbVoyelles(mot):
  if len(mot)==0:
    return None
  cpt=0
  for lettre in (len(mot)):
    if lettre in 'aeiouy':
      cpt=cpt+1
  return cpt