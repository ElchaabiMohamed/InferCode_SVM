def minimum(lst):
   if len(lst) == 1:
      return lst[0]

   mini = minimum(lst[1:])
   if lst[0] < mini:
      return lst[0]
   else:
      return mini



def main():
   min = None
   print((minimum([6,5,1,3,4])))
   print((minimum([6,5,11,3,4])))
   print((minimum([6,15,11,13,14])))
   print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
   main()

# 1
# 3
# 6
# 4