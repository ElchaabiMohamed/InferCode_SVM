import time

def countdown(num):
   while num >= 1:
      print(num)
      time.sleep(0.1)
      num -= 1
   print("LIFT OFF!")
   return num

def search(str,letter):
   if letter in str:
      print(True)
   else:
      print(False)
   

def index(str,letter):
   i = 0
   while i < len(str) and str[i] != letter:
      i += 1
   if letter in str:
      print(i)
   else:
      print('-1')
   

'''
if __name__ == '__main__':
   countdown(10)
   search('python','y')
   index('python','y')
'''
