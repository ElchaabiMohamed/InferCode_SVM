def somme(liste):
  res=0
  if len(liste)==0:
    return 0
  else:
    for elem in liste:
    	res=res+elem
  return res