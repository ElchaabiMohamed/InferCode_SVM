def minimum(list):
   if len(list) == 1:
      return list[0]
   else:
      if list[-1] < list[0]:
         list.pop(0)
      else:
         list.pop(-1)
      return minimum(list)

if __name__ == '__main__':
   print((minimum([1,2,3,4])))