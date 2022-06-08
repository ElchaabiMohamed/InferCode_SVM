def rechercheDicho(liste,val):
  nbAcces=0
  index=None
  found = False
  acces=int(len(liste)/2)
  while not found and (acces!=0 or acces!=len(liste)):
    nbAcces+=1
    if liste[acces]==val:
      found=True
      index = acces
    elif val<acces:
        acces=int(acces/2)
    else:
      acces=len(liste)-int(acces/2)-1
  return (index,nbAcces)