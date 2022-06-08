def fusion(liste1,liste2):
    a1,a2 = 0,0
    res = []
    while a1 < len(liste1) and a2 < len(liste2):
        if liste1[a1] < liste2[a2]:
            res.append(liste1[a1])
            a1 += 1
        elif liste2[a2] <= liste1[a1]:
            res.append(liste2[a2])
            a2 += 1
    if a1 < len(liste1):
        res.append(liste1[-1])
    elif a2 < len(liste2):
        res.append(liste2[-1])
    return res