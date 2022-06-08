def quatrePlus100(liste):
  res=[]
  x=1
  while len(res)<4 :
    if liste[x]>100 :
      res=res+[liste[x]]
    x=x+1
  return res