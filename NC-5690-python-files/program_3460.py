def suiteGeo(liste):
  i=0
  res=True
  if len(liste)==1 and liste[0]!=0:
    res=True
  if len(liste)>=2 and liste[0]==0:
    res=False
  if len(liste)==0:
    res=True
  else:
    end=False
    while i<len(liste)-1 and end==False:
      r=liste[0]/liste[1]
      if liste[i]/liste[i+1]==r:
        res=True
      else:
        res=False
        end=True
      i+=1
  return res
  