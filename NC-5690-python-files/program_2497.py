def prononcable(mot):
  voy=('a','e','i','o','u','y')
  con=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z')
  cptcon=0
  cptvoy=0
  res=True
  for i in range(1-len(mot)):
    if mot[i] in voy and mot[i+1] in voy:
      cptvoy+=1
    if mot[i] in con and mot[i+1] in con:
      cptcon+=1
    if cptcon>2 or cptvoy>2:
      res=False
  return res