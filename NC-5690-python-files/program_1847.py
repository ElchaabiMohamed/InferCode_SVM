def suiteGeo(liste):
  i=0
  end=False
  res=True
  while i<len(liste)-1 and res==True and end==False:
    if liste[i]==0:
      res=False
    elif len(liste)==1 and liste[i]>=1:
      end=True
      res=True
    else:
      q=liste[1]/liste[0]
      if liste[i+1]/liste[i]==q:
        res=True
      else:
        res=False
    i+=1
  return res