def sommeNPremiersEntiersPairs(n):
  
  somme=0
  for elem in range(1,n+1):
    if elem%2==0:
      somme=somme+elem
  return somme
    