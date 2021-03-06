import sys

def reverse_list(a):
    if a == []:
        return []

    return [a[-1]] + reverse_list(a[:-1])

def main():
    print((reverse_list([1])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
