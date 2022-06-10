import sys

def reverse_list(a):
    if a == []:
        return []
    elif len(a) == 1:
        return a    
    else:
        b = [reverse_list(a[1:])]
        return b.append(a[0])
def main():
    print((reverse_list([1])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
