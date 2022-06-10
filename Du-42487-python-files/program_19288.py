def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)



def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()
