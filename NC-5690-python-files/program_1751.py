def fusion(liste1,liste2):
  i=0
  j=0
  res = []
  while j<len(liste2) and i<len(liste1):
    if liste1[i]<liste2[j]:
      res.append(liste1[i])
      i+=1
    else:
      res.append(liste2[j])
      j+=1
  return res