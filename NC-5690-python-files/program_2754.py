def suiteAriGeo(liste):
  a=0
  b=0
  if len(liste)>1:
    suite=liste[0]
    i=1
    res=True
  while i<len(liste)-1 and res==True:
    suite=a*suite+b
    if suite==liste[i]:
      res=True
    else:
      res=False
    i+=1
  return res