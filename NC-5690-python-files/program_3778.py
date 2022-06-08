def nbSyllabes(mot):
  cpt=0
  for i in range(0,len(mot)-1):
    if (mot[i] in 'aeiouy') and not(mot[i+1] in 'aeiouy'):
      cpt+=1
  return cpt