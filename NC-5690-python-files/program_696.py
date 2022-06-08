def maximum(liste):
    if len(liste)==0:
      max=None
    else:
      max=liste[0]
      for i in range(liste):
        if liste[i]>max:
          max=liste[i]
    return max
  