def compare(chaine1,chaine2):
    if chaine1=='':
      res=-1
    elif chaine2=='':
      res=1
    else:
      res=0
      i=0
      mmlttr=0
      while i<len(chaine1) and i<len(chaine2):
        if chaine1[i]>chaine2[i]:
          res=-1
        elif chaine1[i]<chaine2[i]:
          res=1
        else:
          mmlttr=mmlttr+1
        i=i+1
      if len(chaine1)>len(chaine2):
        if len(chaine2)==mmlttr:
          res=1
      elif len(chaine1)<len(chaine2):
        if len(chaine1)==mmlttr:
          res=-1
    return res