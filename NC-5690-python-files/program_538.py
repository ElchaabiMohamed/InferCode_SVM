def produitScalaire(vec1,vec2):
    res = 0
    if len(vec1) == 0 or len(vec2) == 0:
        res = 0
    else:
        for i in range(len(vec1)):
            res += vec1[i] * vec2[i]
    return res