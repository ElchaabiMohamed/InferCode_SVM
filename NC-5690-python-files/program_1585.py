def fusion(liste1,liste2):
  res=[]
  i=0
  while i<len(liste1)+len(liste2):
    if liste1[i]>liste2[i]:
      res+=[liste2[i]]
    elif liste1[i]<liste2[i]:
      res+=[liste1[i]]
    else:
      res+=[liste[i]]+[liste[i]]
  return res