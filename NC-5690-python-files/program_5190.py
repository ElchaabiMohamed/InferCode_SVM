def nbChiffres(nombre):
 cpt=0
 while nombre!=0:
    nombre=nombre//10
    cpt=cpt+1
    return cpt 