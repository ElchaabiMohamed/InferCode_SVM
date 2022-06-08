def produitScalaire(vec1,vec2):
  res=0
  i1=0
  i2=0
  while i1<len(vec1) and i2<len(vec2):
    res=res+(vec1[i1]*vec2[i2])
  if vec1==[] and vec2==[]:
    res=0
  return res