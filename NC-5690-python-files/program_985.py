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

  if len(liste1)>len(liste2):
    for ind in range (i,len(liste1)):
      listefusion.append(liste1[ind])

  if len(liste2)>len(liste1):
    for ind in range (j,len(liste2)):
      listefusion.append(liste2[ind])
  return listefusion
