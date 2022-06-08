def bissextile(annee):
  if annee%400 == 0 or (annee%4 == 0 and annee%100 != 0) :
    res = True
  else :
    res = False
    
  return res