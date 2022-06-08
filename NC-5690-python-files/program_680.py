def ecart(liste):
  min=0
  max=0
  if liste==[]:
    res=None
  elif len(liste)==1:
    res=0
  else:
    for elem in liste:
      if elem<=min:
        min=elem
      elif elem>=max:
        max=elem
    res=max-min
  return res