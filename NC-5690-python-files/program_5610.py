def bissextile(a):
    if a%4==0 and a%400==0: 
      res=True
    elif a%4==0 and a%100!=0: 
      	res=False
    else: 
      	res=False
    return res