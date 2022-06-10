
def count_letters(s, l=None):
    if l == None:
        l = []
    if not s:
        return sum(l)
    l.append(1)
    s = s[1:]
    return count_letters(s,l)