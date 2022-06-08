def nbVoyelles(mot):
  res=0
  for i in range(len(mot)):
    if mot[i] in ['a','e','i','o','u']:
      res=res+1
    return res