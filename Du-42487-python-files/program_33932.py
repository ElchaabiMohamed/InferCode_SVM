import time

def countdown(count):
    while (count >= 1):
        print(count) 
        time.sleep(0.1)
        count -= 1
    print ("LIFT OFF!")

if __name__ == '__main__':
   countdown(3)


def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
        return True
      i += 1
   return False


def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
        return i
      i += 1
   return - 1
       




