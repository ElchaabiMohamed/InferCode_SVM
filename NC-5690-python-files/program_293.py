def fusion(liste1,liste2):
  liste=[]
  liste.extend(liste1)
  liste.extend(liste2)
  i=1
  n=0
  res=[]
  while i<len(liste) :
    if liste[i-1]>liste[i] :
      res.append(liste[i])
      if liste[i-1]>n :
        n=liste[i-1]
    elif liste[i-1]<liste[i] :
      res.append(liste[i-1])
      if liste[i]>n :
        n=liste[i]
    i=i+1
  res.append(n)
  
  return res