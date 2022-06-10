import time

def countdown(count):
 while (count >=1):
  print(count)
  time.sleep(0.1)
  count -= 1
 print ("LIFT OFF!")

if __name__ == '__main__':
   countdown(3)
