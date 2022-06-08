def nbSyllabes(mot):
  if mot=='':
    cpt=0
  else:
    cpt=0
    if mot[0] in 'aeiouy':
      cpt+=1
    for i in range(1,len(mot)):
      if mot[i] in 'aeiouy' and mot[i-1] not in 'aeiouy':
        cpt+=1
    if mot[-1]=='e' or (mot[-1]+mot[-2]) not in 'aeiouy':
      cpt-=1
    if cpt==0:
      cpt+=1
  return cpt