def moyenne(liste):
  if len(liste) == 0 :
    res = None
  else :
    res = 0
    for elem in liste :
    	res = res + elem
    res = res/len(liste)  
  return res