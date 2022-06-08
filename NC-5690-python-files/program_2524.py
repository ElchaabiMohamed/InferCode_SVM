def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and j<len(liste2):
    if liste1[i]<liste2[j]:
      res.append(liste1[i])
      i=i+1
    else:
      res.append(liste2[j])
      j=j+1
  if len(liste1)!=len(liste2):
    if len(liste1)>len(liste2):
      for k in range(len(liste2),len(liste1)):
        res=res+liste1[k]
    elif len(liste1)<len(liste2):
      for k in range(len(liste1,len(liste2))):
        res=res+liste2[k]
  return res