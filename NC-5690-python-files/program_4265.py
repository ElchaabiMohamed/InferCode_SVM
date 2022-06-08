def nbVoyelles(mot):
  res=0
  for i in range(len(mot)):
    if mot[i]==('a,e,y,u,i,o'):
      res=res+1
  return res