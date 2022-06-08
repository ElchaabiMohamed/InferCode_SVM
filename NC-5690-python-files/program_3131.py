def nbVoyelles(mot):
  res=0
  for i in range(len(mot)):
    if mot[i] in 'aeiouy':
      res=res+1
  return None