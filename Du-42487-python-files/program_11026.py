def maximum(list):
   if len(list) == 1:
      return list[0]
   else:
      if list[-1] < list[0]:
         list.pop(-1)
      else:
         list.pop(0)
      return maximum(list)

if __name__ == '__main__':
   print((maximum([1,2,3,4])))