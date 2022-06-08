def quatrePlus100(l):
  res=[]
  i=0
  while i<len(l) and len(res)<4:
      if l[i]>100:
         res=res+[l[i]]
      i=i+1
  return res