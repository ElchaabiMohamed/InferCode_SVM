def sommeNbPairs(liste):
  res= 0
  if liste== []:
    res= 0
  else:
    for i in liste:
      if i%2 == 0:
        res= res + i
  return res