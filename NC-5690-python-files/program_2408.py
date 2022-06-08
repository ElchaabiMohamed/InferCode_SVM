def ecart(liste):
    if len(liste)==0:
      res=None
    else:
      min=l[0]
      for i in range(1,len(l)):
        if l[i]<min:
          min=l[i]
      max=l[0]
      for i in range(1,len(l)):
        if l[i]>max:
          max=l[i]
    res=max-min
    return res