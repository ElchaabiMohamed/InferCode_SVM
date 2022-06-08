def rechercheDicho(liste,val):
  nbAcces=0
  index=None
  found = False
  acces=int(len(liste)/2)
  while not found:
    nbAcces+=1
    if acces==val:
      found=True
    elif val<acces:
        acces=int(acces/2)
    else:
      acces=int(len(liste)-(acces/2))
  for i in liste:
    if i == val:
      index=i
  return (index,nbAcces)