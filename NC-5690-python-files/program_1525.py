def sousChaine(s1,s2):
    if s1 == '':
        res = True
    elif s1 in s2:
        res = True
    else:
        res = False
    return res