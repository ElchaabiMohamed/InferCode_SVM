def compare(chaine1,chaine2):
    if chaine1=='':
      res=-1
    elif chaine2=='':
      res=1
    else:
      res=0
      i=0
      while i<len(chaine1) and i<len(chaine2) and res==0:
        if chaine1[i]<chaine2[i]:
          res=-1
        elif chaine1[i]>chaine2[i]:
          res=1
        i=i+1
      mmlttr=0
      if res==0:
        i=0
        if len(chaine1)>len(chaine2):
          for i in range(len(chaine1)):
            if chaine1[i]==chaine2[i]:
              mmlttr=mmlttr+1
        elif len(chaine1)<len(chaine2):
          for i in range(len(chaine2)):
            if chaine1[i]==chaine2[i]:
              mmlttr=mmlttr+1
      if len(chaine1)>len(chaine2):
        if len(chaine2)==mmlttr:
          res=1
      elif len(chaine1)<len(chaine2):
        if len(chaine1)==mmlttr:
          res=-1
    return res