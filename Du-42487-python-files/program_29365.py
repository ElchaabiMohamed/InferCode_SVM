def reverse_list(l):
    if l==[]:
        return None
    return l[::-1]

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([])))

if __name__ == '__main__':
    main()