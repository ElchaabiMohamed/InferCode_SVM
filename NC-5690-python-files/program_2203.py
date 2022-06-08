def prononcable(mot):
  res=True
  cpt=0
  i=0
  while i<len(mot) and res:
    if elem not in 'aeiouy':
      cpt+=1
    elif elem in 'aeiouy':
      cpt=0
    elif cpt>=3:
      res=False
    i+=1
  return res