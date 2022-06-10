def maximum(a):
   if len(a) == 1:
      return a[-1]
   elif a[0] > a[-1]:
      return maximum(a[:-1])
   elif a[0] < a[-1]:
      return maximum(a[1:])

def main():
    min = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
