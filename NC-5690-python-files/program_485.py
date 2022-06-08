def fusion(liste1,liste2):
    if liste1==[]:
      res=liste2
    elif liste2==[]:
      res=liste1
    else:
      res=[]
      i=0
      j=0
      while i<len(liste1) and j<len(liste2):
        if liste1[i]<liste2[j]:
          res.append(liste1[i])
          i=i+1
        else:
          res.append(liste2[j])
          j=j+1
      if len(liste1)>len(liste2):
        while i<len(liste1):
          res.append(liste1[i])
          i=i+1
      elif len(liste1)<len(liste2):
        while j<len(liste2):
          res.append(liste2[j])
          j=j+1
    res.sort()
    return res