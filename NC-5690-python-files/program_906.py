def nbVoyelles(mot):
  res=0
  for i in range(len(mot)):
    if mot[i]=='aeyuio':
      res=res+1
  return res