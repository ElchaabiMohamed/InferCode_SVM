def nextConway(s):
    res = ""
    nb = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            nb+=1
        else:
            res += str(nb)+s[i]
            nb = 1
    res+= str(nb)+s[i+1]
    return res