def minimum(l):
    def lowest(first, rest):
        if len(rest) == 0:
            return first
        if first > rest[0] or first < 0:
            return lowest(rest[0], rest[1:])
        else:
            return lowest(first, rest[1:])
    return lowest(l[0], l[1:])