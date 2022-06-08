def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and i<len(liste2):
    if liste1[i]<liste2[j]:
      res.append(liste1[i])
      j=i+1
    else:
      res.append(liste1[i])
      i=i+1
      while j<len(liste2):
        res.append(liste2[j])
        j=j+1
      
      while 1<len(liste1):
          res.append(liste1[i])
          i=i+1
  return res