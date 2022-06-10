def minimum(a):
    if len(a) == 1:
        return a[0]
    if a[0] < a[1]:
    	a.remove(a[1])
    else: 
    	a.remove(a[0])
    return(minimum(a))


def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
