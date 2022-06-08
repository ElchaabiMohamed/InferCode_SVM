def sommeNPremiersEntiers(n):
  if n <= 0:
    return 0
  else:
    sum = 0
    for i in range(1,n+1):
      sum += i
    return sum