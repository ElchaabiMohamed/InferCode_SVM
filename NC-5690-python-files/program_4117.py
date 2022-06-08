def fusion(liste1,liste2):
  liste=[]
  liste.extend(liste1)
  liste.extend(liste2)
  i=0
  n=liste[0]
  res=[]
  while i<len(liste) :
    if n>liste[i] :
      res.append(liste[i])
    elif n<liste[i] :
      res.append(n)
      n=liste[i]
    i=i+1
  
  return res