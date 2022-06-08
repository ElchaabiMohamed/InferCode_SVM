def moyenne(liste):
  if len(liste) == 0 :
    res = None
  res = 0
  for elem in liste :
    res = res + liste
  res = res/len(liste)  
  return res