def produitScalaire(vec1,vec2):
  res=0
  i=0
  while i<len(vec1) and i<len(vec2) :
    res= res+(vec1[elem]*vec2[elem])
    i=i+1
  return res