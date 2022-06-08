def prononcable(mot):
  cpt=0
  res=True
  for i in range(len(mot)):
    if mot[i] in ('a','e','i','o','u','y'):
      cpt+=1
    if cpt>3:
      res=False
  return res