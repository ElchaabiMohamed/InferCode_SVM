def bissextile(a):
    if a%4==0: 
      res=True
    elif a%400==0:
      res=True
    elif a%100!=0: 
      res=False
    else: 
      	res=False
    return res