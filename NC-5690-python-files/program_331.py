def stockerChiffres(n):
  res=[]
  if n==0:
    res.append(n)
  while n!=0:
    res.append(n%10)
    n=n//10
  return res