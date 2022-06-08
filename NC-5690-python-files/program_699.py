def nbSyllabes(mot):
    cpt=0
    if mot[0] in 'aeiouy':
      cpt+=1
    for i in range(1,len(mot)):
      if mot[i] in 'aeiouy' and mot[i-1] not in 'aeiouy':
        cpt+=1
    if mot[-1]=='e':
      cpt-=1
    if cpt==0:
      cpt+=1
    if mot=='':
      cpt=0
    return cpt