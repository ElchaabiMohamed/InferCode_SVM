def power(n,p):
    def sub_power(n,p):
        if p == 0:
            return 1
        if p == 1:
            return n
        return n ** p-1
    if sub_power(n,p) + 1 == 1:
        return 2
    return sub_power(n,p) + 1