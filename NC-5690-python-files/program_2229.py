def bissextile(annee):
  if annee%4==0 and annee%100!=0:
    if annee%400==0:
      return True
  else:
    return False
