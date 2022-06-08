def bissextile(annee):
  if annee%4==0 and not annee%100!=0 or annee%400==0:
    res=True
  else:
    res=False
  return res