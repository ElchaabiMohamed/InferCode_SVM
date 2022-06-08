def nbVoyelles(mot):
  if len(mot)==0:
    return None
  compteur=0
  for element in mot:
    if element in 'aeiouy':
      compteur=compteur+1
  return compteur