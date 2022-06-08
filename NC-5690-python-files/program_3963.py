def rechercheDicho(liste,val):
  min = 0
  max = len(liste)
  index = None
  nbAcces=0
  acces =(max+min)//2
  found = False
  while max!=acces and min!=acces and not found:
    nbAcces+=1
    print (nbAcces)
    print(acces)
    if liste[acces]==val:
      found = True
      index = acces
    else:
      if liste[acces]>val:
        max = acces
      else:
        min = acces
      acces = (max+min)//2
  return (index,nbAcces)