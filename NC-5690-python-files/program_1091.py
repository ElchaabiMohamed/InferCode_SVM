def indiceOccurrence(n,x,liste):
  cpt = 0
  find = False
  i = 0
  while i<len(liste) and find == False :
    if liste[i]==x:
      cpt = cpt + 1
    if cpt == n : 
      find = True
    i = i + 1
  if find == True :
    return i-1
  else :
    return find