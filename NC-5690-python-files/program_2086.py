def bissextile(annee):
  a=(annee/400)
  b=(annee//400)
  c=(annee/4)
  d=(annee//4)
  e=(annee/100)
  f=(annee//100)
  if a==b or (c==d and e!=f) :
    res=True
  else :
    res=False
    
  return res