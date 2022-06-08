def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and j<len(liste2):
    if liste[i]<liste[j]:
     res.append(i)
    i=i+1
    if liste[i]>=liste[j]:
     res.append(j)
     j=j+1

  return res