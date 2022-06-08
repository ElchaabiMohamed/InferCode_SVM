def distribution(liste,n):
    res=[0]*n
    for i in range(len(liste)):
        if liste[i]==0:
            res[0]=res[0]+1
        elif liste[i]==1:
            res[1]=res[1]+1
        elif liste[i]==2:
            res[2]=res[2]+1
        else:
            res[3]=res[3]+1
    return res


  
  
