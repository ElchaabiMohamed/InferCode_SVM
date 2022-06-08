def maximum(liste):
  res=liste[0]
  for x in liste: 
    if x>res:
      res=x
  return res