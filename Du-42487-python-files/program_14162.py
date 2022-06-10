def fibonacci(number):
    if number == 0 or number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()