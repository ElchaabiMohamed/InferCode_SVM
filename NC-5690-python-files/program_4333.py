def nbVoyelles(mot):
  v='aeiouy'
  cpt=0
  for c in mot:
    if c==v:
      cpt=cpt+1
  return cpt