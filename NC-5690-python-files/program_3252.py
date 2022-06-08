def bissextile(annee):
  res=0
  if annee%100>0:
    if annee%4==0 and annee%400==0:
      res=False
  else:
    res=True
  return res