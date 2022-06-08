def nbSyllabes(mot):
  if len(mot)==0:
    return 0
  else:
    if (mot[0] in 'aeiouy'):
      cpt = 0
    else:
      cpt = 1
    for i in range (0, len(mot)-1):
      if (mot[i] in 'aeiouy') and not(mot[i+1] in 'aeiouy'):
        cpt+=1
    return cpt
        