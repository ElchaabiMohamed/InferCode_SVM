def reverse_list(l):
   if l == []:
      return []
   temp = reverse_list(l[1:])
   temp.append(l[0])
   return temp

#from reverse_102 import reverse_list

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()