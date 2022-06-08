def rendezVous(debut1,fin1,debut2,fin2):
    if fin2 <= fin1 and fin2 >= debut1:
        return True
    elif fin1 <= fin2 and fin1 >= debut2:
        return True
    else:
        return False