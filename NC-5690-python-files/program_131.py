def bissextile(annee):
  res=False
  if annee%4==0 and annee%100!=0:
    res=True
  elif annee%400==0:
    res=True
  return res