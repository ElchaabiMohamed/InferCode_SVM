def bissextile(annee):
    if annee%4==0 :
      res=True 
    else :
      res=False
    if annee%400==0 :
      res=True
    else :
      res=False
    return res