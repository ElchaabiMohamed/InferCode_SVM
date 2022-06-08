def maximum(liste):
  res=liste[1]
  for x in liste: 
    if x>res:
      res=x
  return res