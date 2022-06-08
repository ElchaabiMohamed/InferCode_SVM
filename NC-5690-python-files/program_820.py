def fusion(liste1,liste2):
  i=0
  j=0
  listefusion=[]
  if len(liste1)==0:
    listefusion=liste2
  elif len(liste2)==0:
    listefusion=liste1
  
  while i<len(liste1) and j<len(liste2):
    if liste1[i]>liste2[j]:
      listefusion.append(liste2[j])
      j=j+1
    else:
      listefusion.append(liste1[i])
      i=i+1
  
  if len(liste1)>0 and len(liste2)>0:
    if max(liste1)>max(liste2):
      for ind in range (i+1,len(liste1)):
        listefusion.append(liste1[ind])

    if max(liste2)>max(liste1):
      for ind in range (j+1,len(liste2)):
        listefusion.append(liste2[ind])

  return listefusion
  
