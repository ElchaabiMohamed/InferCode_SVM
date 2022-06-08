def fusion(liste1,liste2):
  res=[]
  i=0
  j=0
  while i<len(liste1) and j<len(liste2):
    if liste1[i]>liste2[j]:
      res.append(liste2[j])
      j+=1
    else :
      res.append(liste1[i])
      i+=1
  #post traitement 
  while j<len(liste2): #finir de rajouter tous les éléments de liste2
    res.append(liste2[j])
    j+=1
  while i<len(liste1): #finir de rajouter tous les éléments de liste1
    res.append(liste1[i])
    i+=1
  return res
   