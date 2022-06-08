def nbVoyelles(mot):
  if len(mot)==0:
    res=0
  else:
    for elem in mot:
      res=0
      if elem in 'aeiouy':
        res=res+1
  return res     