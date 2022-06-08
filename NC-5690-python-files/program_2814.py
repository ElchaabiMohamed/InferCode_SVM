def maximum(liste):
  maxi = liste[0]
  for i in liste:
    if i >= maxi:
    	maxi = i
  return maxi