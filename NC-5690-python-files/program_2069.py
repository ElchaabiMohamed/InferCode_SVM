def bissextile(a):
    if a%4==0 or a%400==0: 
      res=True
    else: 
      res=False
    return res