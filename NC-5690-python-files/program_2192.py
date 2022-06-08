def rechercheDicho(liste,val):
  index = None
  nbAcces=0
  acces =len(liste)//2
  prevAcces = -1
  found = False
  while acces !=prevAcces and not found:
    nbAcces+=1
    if liste[acces]==val:
      found = True
      index = acces
    else:
      prevAcces = acces
      if liste[acces]>val:
        acces = acces//2
      else:
        acces = len(liste)-1-(acces//2)
  return (index,nbAcces)