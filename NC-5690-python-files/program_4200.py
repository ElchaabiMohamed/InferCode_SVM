def sommeNPremiersEntiersPairs(n):
  somme=0
  for i in range(1,n+1):
      somme=somme+i
  for elem in liste:
    if elem%2==0:
      somme=somme+elem
  return somme
    