def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and j<len(liste2):
    if liste1[i]<liste2[j]:
      res.append(liste1[i])
    else:
      res.append(liste2[j])
    i+=1
    j+=1
    return res