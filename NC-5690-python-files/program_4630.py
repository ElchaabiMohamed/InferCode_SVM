def rechercheDicho(liste,val):
  min = 0
  max = len(liste)-1
  index = None
  nbAcces=0
  acces =(max+min)//2
  found = False
  while min<max and not found:
    nbAcces+=1
    print (nbAcces)
    print(liste[acces])
    if liste[acces]==val:
      found = True
    else:
      if liste[acces]>val:
        max = acces
      else:
        min = acces
      acces = (max+min)//2
  if found :
    return (index,nbAcces)
  return(None,nbAcces)