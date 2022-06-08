from math import sqrt
def polynome(a, b, c):
    Delta = (b ** 2) - (4 * a * c)
    if Delta < 0:
        return ("pas de solution")
    else:
        if Delta == 0:
            sol = -b / (2 * a)
            return (sol)
        else:
            sol1 = (-b - sqrt(Delta)) / 2 * a
            sol2 = (-b + sqrt(Delta)) / 2 * a
            return (sol2, sol1)