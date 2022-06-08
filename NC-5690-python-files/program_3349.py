def prononcable(mot):
  res=True
  x="aeiouy"
  cpt=0
  i=0
  while i<len(mot) and not x:
    cpt+=1
    i+=1
  if cpt>3:
    res=False
  return res