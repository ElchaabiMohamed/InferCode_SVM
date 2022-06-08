def nbVoyelles(mot):
  v='aeiouy'
  cpt=0
  for c in mot:
    if c in v:
      cpt=cpt+1
  return cpt