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
  if j==len(liste2):
    while i<len(liste1):
      listefusion.append(liste1[i])
      i=i+1
  if i==len(liste1):
    while j<len(liste2):
      listefusion.append(liste2[j])
      j=j+1
  
  return listefusion
    
    
