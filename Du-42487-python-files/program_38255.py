import sys

def reverse_list(list):
    if list == []:
        return []
    elif len(list) == 1:
        return [].append(list)
    else:
        return reverse_list(list[1:]).append(list[0])

def main():
    print((reverse_list([1])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
