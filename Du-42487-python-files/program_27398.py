def maximum(l,current_max = None):
    if not l:
        return current_max
    first=l.pop()
    if current_max==None or first>current_max:
        return maximum(l,first)
    return maximum(l,current_max)

def main():
    min = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([5, 3, 1, 1, 3, 7, 12, 21, -43, 65, -44, 32, 12, 65, 55])))

if __name__ == '__main__':
    main()