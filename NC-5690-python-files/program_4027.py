def nbVoyelles(mot):
  res=0
  for i in range(len(mot)):
    if i in 'aeyuio':
      res=res+1
  return res