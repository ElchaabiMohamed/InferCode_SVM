def quatrePlus100(liste):
  res = []
  cpt=0
  for i in liste:
    if i>=100 and cpt!=4:
      res.append(i)
      cpt+=1
  return res
