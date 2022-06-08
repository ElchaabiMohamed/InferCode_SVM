def fusion(liste1,liste2):
  res= []
  res.extend(liste1)
  res.extend(liste2)
  for i in range(len(res)):
    for j in range(0,len(res)-i-1):
      if res[j]>res[j+1]:
        res[j],res[j+1] = res[j+1], res[j]
  return res