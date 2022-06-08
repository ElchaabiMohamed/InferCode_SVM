def maximum(liste):
  res='None'
  for elem in liste :
    if elem>res :
      res=res+elem
  return res