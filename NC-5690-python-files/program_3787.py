def  rechercheDicho(liste,val):
  found=False
  min=0
  nbAcces=0
  max=len(liste)-1
  while min<max and not found:
    acces=(min+max)//2
    n=liste[acces]
    nbAcces+=1
    if n==val:
      found=True
    elif n<val:
      min=acces+1
    else:
      max=acces-1
  if found:
    return (acces,nbAcces)
  return (None,nbAcces)
