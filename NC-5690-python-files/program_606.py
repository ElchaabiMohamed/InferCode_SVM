def nbVoyelles(mot):
  n = 0
  for i in mot:
    if i in 'aeiouy':
      n+=1
  return n