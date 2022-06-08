def nbVoyelles(mot):
  res=0
  for lettre in range(len(mot)):
    if lettre in aeiouy:
       res=res+1
  return res