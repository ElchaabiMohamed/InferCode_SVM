def fusion(liste1,liste2):
  i=0
  j=0
  listefusion=[]
  while i<len(liste1) and j<len(liste2):
    if liste1[i]>liste2[j]:
      listefusion.append(liste2[j])
      j=j+1
    else:
      listefusion.append(liste1[i])
      i=i+1

  if max(liste1)>max(liste2):
    for ind in range (i,len(liste1)):
      listefusion.append(liste1[ind])

  if max(liste2)>max(liste1):
    for ind in range (j,len(liste2)):
      listefusion.append(liste2[ind])
  return listefusion
