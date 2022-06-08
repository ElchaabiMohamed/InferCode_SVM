def premier(n):
  res=True
  if n==0 or n==1:
    return False
  for i in range(2,n-1): 
    if n%i==0:
      res=False
  return res

def nombresPremiers(n):
  liste=[]
  i=0
  while len(liste)<n:
    if premier(i)==True:
      liste.append(i)
    i+=1
  return liste