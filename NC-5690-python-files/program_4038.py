def nbVoyelles(mot):
  res = 0
  for elem in mot :
    if elem in "aeiouy":
      res = res + 1
  return res