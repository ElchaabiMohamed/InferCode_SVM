def minimum(liste):
  res=liste[0]
  for i in liste: 
    if i<res:
      res=i
    else:
      res=None
  return res