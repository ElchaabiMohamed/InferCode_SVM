def rechercheDicho(liste,val):
  index = None
  nbAcces=0
  acces = int(len(liste)/2)
  found = False
  while acces in range(len(liste)) and not found:
    nbAcces+=1
    if liste[acces]==val:
      found = True
      index = acces
    elif liste[acces]>val:
      acces = int(acces/2)
    else :
      acces = len(liste)-1-int(acces/2)
  return (index,nbAcces)