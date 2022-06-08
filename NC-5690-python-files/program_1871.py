def quatrePlus100(liste):
  res=[]
  i = 0
  while i<len(liste) and len(res)<4:
    if liste[i]>100:
      res=res+[liste[i]]
    i=i+1
  return res 