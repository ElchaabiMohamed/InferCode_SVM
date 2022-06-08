def nombresPremiers(n):
  res = []
  cpt = 2
  isPrime = True
  while len(res)<n:
    while not isPrime:
      cpt+=1
      isPrime=True
      for i in range(2,cpt):
        if cpt%i==0:
          isPrime=False
    res.append(cpt)
  return res