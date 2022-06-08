def premier(n) :
  res=True
  for div in range(2,n):
    if n%div==0:
      res=False
  return res

def nombresPremiers(n):
  nbPrem=[]
  i=2
  while n!=0:
    if premier(i):
      nbPrem+=[i]
      n-=1
    i+=1
  return nbPrem