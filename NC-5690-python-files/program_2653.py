def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and j<len(liste2):
    if liste1[i]<liste2[j]:
      res=res+[liste1[i]]
      i=i+1
    elif liste2[j]<liste1[i]:
      res=res+[liste2[j]]
      j=j+1
    else:
      res=res+[liste1[i]]
      res=res+[liste2[j]]

  if i<len(liste1):
    while i<len(liste1):
      res=res+[liste1[i]]
      i=i+1
  else:
    while j<len(liste2):
      res=res+[liste2[j]]
      j=j+1
  return res