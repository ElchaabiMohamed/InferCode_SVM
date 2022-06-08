def suiteGeo(liste):
  if len(liste)==0:
    res=True
  elif len(liste)==1 and liste[0]!=0:
    res=True
  else:
    if liste[0]==0:
      res=False
    else:
      i=0
      End=False
      while i<len(liste)-1:
        r=liste[1]/liste[0]
        if liste[i+1]/liste[i]==r and End==False:
          res=True
        else:
          res=False
          End=True
        i+=1
  return res