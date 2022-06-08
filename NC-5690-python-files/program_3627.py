def produitScalaire(vec1,vec2):
  i=0
  res=0
  while i<len(vec1) and i<len(vec2):
    res = res+(vec1[i]*vec2[i])
  i=i+1
  return res
