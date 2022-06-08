def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and j<len(liste2):
    if liste1[i]<liste2[j]:
      res=res+[liste1[i]]
      i+=1
    else:
      res=res+[liste2[j]]
      j+=1
  while i<len(liste1) or j<len(liste2):
    if i<len(liste1):
      res.append(liste1[i])
      i+=1
    elif j<len(liste2):
      res.append(liste2[j])
      j+=1
  return res