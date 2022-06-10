import time
def countdown(num):
   while num >= 1:
      print(num)
      num = num - 1
      time.sleep(0.1)
   
def search(str,letter):
   if letter in str:
      print("True")
   else:
      print("False")

def index(str,letter):
   i = 0
   if letter in str:
      letter = letter[0]















if __name__ == '__main__':
   print('calling countdown(\'10\')')
   countdown(2)
   print("LIFT OFF!")
   search("python","a")
   

