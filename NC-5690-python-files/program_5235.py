def nbSyllabes(mot):
  res=0
  for i in range (len(mot)):
    if mot[i-1] not in 'aeiouy' and mot[i] in 'aeiouy':
      res=res+1
  if mot[-1] not in 'aeiouy':
    res=res-1
  
  return res