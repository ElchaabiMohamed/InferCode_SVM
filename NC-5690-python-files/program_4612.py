def nbVoyelles(mot):
  res=0
  for elem in mot:
    if elem=='aeiouy':
      res+=1
  return res