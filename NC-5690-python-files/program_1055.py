def maximum(liste):
    n = len(liste)
    maxi = liste[0]
    for i in range(1,n):
      if liste[i] >= maxi:
    	  maxi = liste[i]
    return maxi