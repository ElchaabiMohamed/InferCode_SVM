def plusLongueSuite(liste):
  cpt=0
  res=0
  for n in liste:
    while n==n:
      cpt=cpt+1
    if n!=n:
      cpt=0
  if res<cpt:
    res=cpt
  
    return cpt