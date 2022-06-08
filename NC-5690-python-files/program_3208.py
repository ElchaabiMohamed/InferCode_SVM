def prononcable(mot):
  res=True
  cpt=0
  i=0
  while i<len(mot) and res:
    if mot[i] not in 'aeiouy':
      cpt+=1
    elif mot[i] in 'aeiouy':
      cpt=0
    if cpt>3:
      res=False
    i+=1
  return res