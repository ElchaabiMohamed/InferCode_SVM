def fusion(liste1,liste2):
    if liste1==[]:
      res=liste2
    elif liste2==[]:
      res=liste1
    else:
      res=[]
      i=0
      while i<len(liste1) and i<len(liste2):
        res=res+[liste1[i]]+[liste2[i]]
      if len(liste1)>len(liste2):
        while i<len(liste1):
          res=res+[liste1[i]]
          i=i+1
      elif len(liste1)<len(liste2):
        while i<len(liste2):
          res=res+[liste2[i]]
          i=i+1
    res.sort()
    return res