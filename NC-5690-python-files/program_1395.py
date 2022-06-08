def produitScalaire(vec1,vec2):
  res=0
  i=0
  j=0
  while i<len(vec1) and j<len(vec2):
    res=i*j+res
  return res