def nbVoyelles(mot):
  res=0
  for elem in mot:
    if 'aeiouy' in mot:
      res= res+1
    return res