def quatrePlus100(liste):
  i=0
  res=[]
  while i<len(liste) and res<4:
    if liste[i]>100:
      res=res+[liste[i]]
    i=i+1
  return res