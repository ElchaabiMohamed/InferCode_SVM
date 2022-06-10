def maximum(lst):
   if len(lst) == 1:
      return lst[0]

   maxi = maximum(lst[1:])
   if lst[0] > maxi:
      return lst[0]
   else:
      return maxi



def main():
   min = None
   print((maximum([6,5,1,3,4])))
   print((maximum([6,5,11,3,4])))
   print((maximum([6,15,11,13,14])))
   print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
   main()

# 1
# 3
# 6
# 4