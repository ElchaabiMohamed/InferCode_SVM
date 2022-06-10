def reverse_list(l,s = None):
   if s == None:
      s = []
   if l == []:
      return s
   else:
      s.append(l[-1])
      l.remove(l[-1])
      return reverse_list(l,s)

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
