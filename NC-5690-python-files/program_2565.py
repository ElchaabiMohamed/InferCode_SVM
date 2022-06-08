def bissextile(annee):
  res=False
  if annee%4==0 and annee%100!=0 or anne%400==0:
    res=True
  return res