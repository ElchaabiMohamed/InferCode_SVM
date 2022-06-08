def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and i<len(liste2):
    if liste1[i]<liste2[j]:
      res.append(liste2[j])
      j=i+1
    else:
      res.append(liste1[i])
      i=i+1
  
  return res