def compare(chaine1,chaine2):
    res=0
    cpt=0
    while cpt<len(chaine1) and cpt<len(chaine2) and res==0:
        if chaine1[cpt]<chaine2[cpt]:
            res=-1
        elif chaine1[cpt]>chaine2[cpt]:
            res=1
        cpt+=1
       #on gère le cas des chaînes de tailles différentes
    if res==0 :
        if len(chaine1)>len(chaine2):
          res=1
        else:
          res=-1
    return res