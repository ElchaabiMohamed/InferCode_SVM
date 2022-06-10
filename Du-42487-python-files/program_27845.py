#import time
#def countdown(num):
#   if num == 1:
#      print num
#      time.slep(0.1)
#      countdown(num -1)

#if __name__ == "__main__":
#   print "Calling countdown function."
#   countdown(3)

#def search (str, letter):
#   if str == "":
#      return False
#   elif str[0] == letter:
#      return True
#   else:
#      return search(str[1:], letter)#

#if __name__ == "__main__":
 #  print "calling search function"
  # print search ("test", "e")
   #print search ("test", "e")
#
#def index(str, letter, pos):
#   if pos == len(str):
 #     return -1
  # elif str[pos] == letter:
   #   return pos
  # else:
  #    return fibonacci(n -1) + fibonacci(n-2)

#if __name__ == "__main__":
 #  print "calling fibonacci function"
  # print fibonacci(0)
   #print fibonacci(6)


import time 
def countdown(num):
   if num == 0:
      print('LIFT OFF!')
   else:
      print(num)
      time.sleep(0.1)
      countdown(num -1)

def search(ls, val):
   if ls == []:
      return False
   elif ls[0] == val:
      return True
   else:
      return search(ls[1:], val)

def index(str, letter):
   if ls == []: 
      return -1
   elif ls[0] == val:
      return val
   else:
      return search(ls[1:], val)

def fibonacci(n):
   if n == 0: 
      return 0
   elif n == 1: 
      return 1
   else: 
      return fibonacci(n-1) + fibonacci(n-2)
