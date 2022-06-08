def quatrePlus100(liste):
  res=[]
  i=0
  while len(res)<4 :
    if liste[i]>100 :
      res.append(liste[i])
    i=i+1
  return res