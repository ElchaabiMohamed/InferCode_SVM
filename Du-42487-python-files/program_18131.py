def reverse_list(l, new_l = None):
    if new_l is None:
        new_l = []

    if len(l) > 0:
        i = l[0]
        l = l[1:]

        new_l = [i] + new_l

        return reverse_list(l, new_l)
    else:
        return new_l



def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()