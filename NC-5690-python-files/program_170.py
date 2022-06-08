def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<liste1 and j<liste2:
    if liste1[i]<=liste2[j]:
      res.append(liste1[i])
      i+=1
    else:
      res.append(liste2[j])
      j+=1
    if len(liste1)<len(liste2):
      res.append(liste2[j])
      j+=1
    else:
      res.append(liste1[i])
      i+=1
  return res