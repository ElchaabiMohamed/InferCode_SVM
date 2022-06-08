def bissextile(a):
    if a%4==0 or a%400==0: 
      res=True
    else: 
      if a%100!=0: 
      	res=False
    return res