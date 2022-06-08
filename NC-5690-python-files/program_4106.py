from math import sqrt

def polynome(a,b,c):
    delta =  b**2 - (4*a*b)
    print(delta)
    if delta > 0:
        x1 = (-b + sqrt(delta))/2*a
        x2 = (-b - sqrt(delta))/2*a
    elif delta == 0:
        x1 = -b/2*a
        x2 = ""
    else:
        print("delta neg")
    return x1,x2
