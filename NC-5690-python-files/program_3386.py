def compteChiffre(chiffre,nombre):
    res = 0
    nombre_str  = str(nombre)
    chiffre_str = str(chiffre)
    for i in range(len(nombre_str)):
        if chiffre_str == nombre_str[i]:
            res += 1
    return res