def power(m, n, flag = True, m1=None):

    if not n:
        return 1

    if flag:
        m1 = m

    if n == 1:
        return m

    return power(m*m1, n-1, False, m1)


def main():
    print((power(2,3)))
    print((power(4,4)))
    print((power(2,32)))
    print((power(10,3)))
    print((power(8,0)))

if __name__ == '__main__':
    main()
