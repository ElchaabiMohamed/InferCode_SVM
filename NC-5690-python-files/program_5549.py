def nbSyllabes(mot):
  voy='aeiouy'
  if mot=='':
    cpt=0
  else:
    cpt=0
    if mot[0] in voy:
      cpt+=1
    for i in range(1,len(mot)):
      if mot[i] in voy and mot[i-1] not in voy:
        cpt+=1
    if mot[-1]=='e':
      cpt-=1
  return cpt