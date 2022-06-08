def sommeNbPairs(liste):
  if liste == []:
    return 0
  else:
    sum = 0
    for num in liste:
      if num%2 == 0:
        sum += num
    return sum