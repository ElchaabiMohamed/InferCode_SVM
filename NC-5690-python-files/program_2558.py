def nbVoyelles(mot):
  if len(mot)==0:
    return 0
  cpt=0
  for elem in mot:
    if elem in (mot)=='aeiouy':
      cpt=cpt+1
  return cpt