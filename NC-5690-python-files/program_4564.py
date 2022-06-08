def nbVoyelles(mot):
  for elem in mot:
    if elem in 'aeiouy':
      res=res+1
  return res