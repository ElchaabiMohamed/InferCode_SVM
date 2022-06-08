def nbSyllabes(mot):
  if len(mot)==0:
    return 0
  else:
    if (mot[0] in 'aeiouy'):
      cpt = 1
    else:
      cpt = 0
    for i in range (0, len(mot)-1):
      if not(mot[i] in 'aeiouy') and (mot[i+1] in 'aeiouy'):
        cpt+=1
    return cpt
        