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
    print(liste[acces])
    if liste[acces]==val:
      found = True
    else:
      if liste[acces]>val:
        max = acces
      else:
        min = acces
      acces = (max+min)//2
  if found:
    for i in range(len(liste)):
      if liste[i] == val:
        index = i
  return (index,nbAcces)