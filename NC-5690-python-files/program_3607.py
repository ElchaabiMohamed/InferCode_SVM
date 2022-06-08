def maximum(liste):
  res=0
  for elem in liste :
    if elem>res :
      res=res+elem
    else :
      res='None'
  return res