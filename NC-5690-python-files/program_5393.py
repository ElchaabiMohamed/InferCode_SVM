def minimum(liste):
  res=liste[0]
  for n in liste: 
    if n<res:
      res=n
  return res