def bissextile(annee):
    if a%4==0 and a%100==0 or a%400==0:
      res=True
    else: 
      res=False
    return res