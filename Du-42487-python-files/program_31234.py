def minimum(lst):
   if len(lst) == 1:
      return lst[-1]
   elif lst[0] < lst[-1]:
      return minimum(lst[:-1])
   elif lst[0] > lst[-1]:
      return minimum(lst[1:])

def mlstin():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
