def bissextile(a):
    if a%4==0 or a%400==0: 
      res=True
    elif a%100!=0: 
      res=False
    return res