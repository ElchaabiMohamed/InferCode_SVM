def maximum(mylist):
   if len(mylist) == 1:
      return mylist[0]

   if mylist[0] < mylist[1]:
      mylist.remove(mylist[0])
      return minimum(mylist)
   else:
      mylist.remove(mylist[1])
      return minimum(mylist)

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()