def sum_up_to(n):
    if n == 0: # base case : no more calls to sum_up_to()
        return 0
    return n + sum_up_to(n-1)

def main():
    print((sumup(0)))
    print((sumup(1)))
    print((sumup(12)))

if __name__ == '__main__':
    main()

