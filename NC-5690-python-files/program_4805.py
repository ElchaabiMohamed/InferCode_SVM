def nbVoyelles(mot):
  if len(mot)==0:
    return 0
  cpt=0
  for lettre in mot:
    if lettre in mot=='aeiouy':
      cpt=cpt+1
  return cpt
  