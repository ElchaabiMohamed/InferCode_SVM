def reverse_list(m):
    if len(m)==1:
        return m
    else:
        return [m.pop()] + reverse_list(m)




def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
