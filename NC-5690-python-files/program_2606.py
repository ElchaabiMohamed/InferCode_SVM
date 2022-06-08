def nbVoyelles(mot):
  res=0
  for i in range(len(mot)):
    if mot[i]==liste('aeyuio'):
      res=res+1
  return res