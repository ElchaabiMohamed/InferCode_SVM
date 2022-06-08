def fusion(liste1,liste2):
  i=0
  j=0
  res=[]
  while i<len(liste1) and j<len(liste2):
    if liste1[i]<liste2[j]:
      res.append(liste1[i])
      i=i+1
    else:
      res.append(liste2[j])
      j=j+1
  while j<len(liste2):
    res.append(liste2[j])
    j=j+1
  while i<len(liste1):
    res.append(liste1[i])
    i+=1
  return res