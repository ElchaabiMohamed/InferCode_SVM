def indiceOccurence (n,x,l):
  verif = False
  i = 0
  cpt = 0
  res = -1
  while i <len(l) and verif == False :
    res = res + 1
    if l[i] == x :
      cpt = cpt + 1  
    if n == cpt :
      verif = True
    i = i + 1
    
  if verif == False :
    res = None
  return res