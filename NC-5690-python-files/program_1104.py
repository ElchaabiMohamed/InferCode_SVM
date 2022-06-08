def minimum(liste): 
    res=1000
    for i in range (len(liste)) :
      if liste [i] < res :
        res= liste[i]
    return res