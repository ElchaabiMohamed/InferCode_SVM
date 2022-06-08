def fusion(liste1,liste2):
  res=[]
  i=0
  while i<len(liste1)+len(liste2) and len(res)<len(liste1)+len(liste2):
    if [liste1[i]]<[liste2[i]]:
      res=res+[liste1[i]]
    elif liste1[i]==liste2[i]:
      res=res+[liste1[i]]+[liste2[i]]
    else:
      res=res+[liste2[i]]
    i=i+1
  return res