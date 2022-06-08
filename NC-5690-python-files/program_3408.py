def stockerChiffres(nombre):
    res=[]
    decomp=nombre
    while decomp!=0:
      decomp=decomp//10
      res=[decomp]+res
    return res