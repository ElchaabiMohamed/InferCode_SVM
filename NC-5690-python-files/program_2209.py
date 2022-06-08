def quatrePlus100(liste):
  res=[]
  x=0
  while len(res)<4 :
    if liste[x]>100 :
      res=res+[liste[i]]
    i=i+1
  return res