def maximum(liste):
  maxi=liste[0]
  for elem in liste:
    if elem>maxi:
      maxi=elem
  return maxi