def nbSyllabes(mot):
    cpt=0
    v='aeiouy'
    if mot[0] in v:
        cpt += 1
    for i in range(1,len(mot)):
        if mot[i] in v and mot[i-1] not in v:
            cpt+=1
    if mot.endswith('e'):
        cpt-=1
    if cpt==0:
        cpt+=1
    if cpt=='':
      cpt=0
    return cpt
    