def bissextile(annee):
  a=(annee/400)
  b=(annee//400)
  if a==b :
    res=True
  else :
    res=False
    
  return res