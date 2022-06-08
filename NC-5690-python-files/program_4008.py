def nbSup100(l,x):
  res=[]
  i=0
  while i<len(l) and len(res)<=4:
      if l[i]>x:
         res=res+[l[i]]
      i=i+1
  return res